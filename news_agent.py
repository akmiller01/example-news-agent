import os
import asyncio
from typing import List
from pydantic import BaseModel, Field
from browser_use import Agent, Controller, ChatGoogle
from dotenv import load_dotenv

# Load environment variables (ChatGoogle class expects GOOGLE_API_KEY in .env)
load_dotenv()

os.environ["ANONYMIZED_TELEMETRY"] = "false"

# 1. Define the structure you want extracted
# This forces the LLM to return clean JSON data rather than just text.
class NewsItem(BaseModel):
    title: str = Field(..., description="The title of the news post, press release, or blog update.")
    url: str = Field(..., description="The direct URL to the specific news item.")

class NewsExtractionResult(BaseModel):
    company_updates: List[NewsItem]

# 2. The extraction function
async def get_company_news(company_url: str):
    print(f"Checking news for: {company_url}")
    
    # Initialize the LLM, I'm using Gemini Flash but you can plug in many https://docs.browser-use.com/supported-models
    llm = ChatGoogle(model="gemini-3-flash-preview")

    # This prompt guides the browser to act like a human researcher
    task = f"""
    You are a researcher looking for recent company updates.
    1. Go to {company_url}.
    2. Navigate to the 'News', 'Press', 'Blog', or 'Insights' section. 
       (If you don't see it immediately, look in the footer or under 'About Us').
    3. Extract the 5 most recent posts or updates.
    4. Return the Title and URL for each.
    """

    agent = Agent(
        task=task,
        llm=llm,
        controller=Controller(),
        use_vision=True,
        # generate_gif=True,
        # This is the key part: it enforces the schema defined above
        output_model_schema=NewsExtractionResult
    )

    try:
        # The agent will browse, click, and read to find the data
        history = await agent.run(max_steps=20)
        result = history.final_result()
        
        if result:
            parsed_news = NewsExtractionResult.model_validate_json(result)
            return parsed_news.company_updates
            
    except Exception as e:
        print(f"Error extracting news: {e}")
        return []

# Example Usage
async def main():
    companies = [
        ("Apple", "https://www.apple.com/"),
    ]
    for company_name, company_url in companies:
        news = await get_company_news(company_url)
        
        print(f"{company_name} New Results")
        for item in news:
            print(f"    - [{item.title}]({item.url})")

if __name__ == "__main__":
    asyncio.run(main())