# Example News Agent

A small example showing how to extract recent company news using a browsing agent and Google's Generative Language model.

## Requirements

- Python 3.10+
- A Google Cloud API key with the Generative Language API enabled
- See `requirements.txt` for Python dependencies

## Quickstart (Unix / macOS)

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the example environment file and populate your API key:

```bash
cp .env-example .env
# Then open .env and set GOOGLE_API_KEY=YOUR_API_KEY
```

4. Run the example:

```bash
python news_agent.py
```

## Quickstart (Windows - PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy the example environment file and populate your API key:

```powershell
Copy-Item .env-example .env
# Then open .env and set GOOGLE_API_KEY=YOUR_API_KEY
```

4. Run the example:

```powershell
python news_agent.py
```

## .env and Google Cloud setup

- Copy `.env-example` to `.env` as shown above.
- The code expects the API key variable `GOOGLE_API_KEY` in the `.env` file.

Creating an API key and enabling the Generative Language API:

1. Go to the Google Cloud Console: https://console.cloud.google.com/
2. Create or select a project.
3. Open **APIs & Services > Library** and enable the **Generative Language API** (or search for "Generative Language").
4. Open **APIs & Services > Credentials**, create an **API key**, and copy it.
5. Paste the key into your `.env` file as:

```
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

Optionally restrict the API key to the Generative Language API and to specific IPs or referrers for safety.

## Notes

- The `news_agent.py` script uses `GOOGLE_API_KEY` from the environment (loaded via `python-dotenv`).
- The example prints a simple formatted list of recent company updates.

## Example output

When the script runs successfully you should see output similar to:

```
Apple New Results
	- [Major League Soccer kicks off 2026 season on Apple TV](https://www.apple.com/newsroom/2026/02/major-league-soccer-kicks-off-2026-season-on-apple-tv/)
	- [Apple introduces a new video podcast experience on Apple Podcasts](https://www.apple.com/newsroom/2026/02/apple-introduces-a-new-video-podcast-experience-on-apple-podcasts/)
	- [Oceanhorn 3: Legend of the Shadow Sea launches March 5 on Apple Arcade](https://www.apple.com/newsroom/2026/02/oceanhorn-3-legend-of-the-shadow-sea-launches-march-5-on-apple-arcade/)
	- [The biggest hits of Bad Bunny’s Apple Music Super Bowl LX Halftime Show](https://www.apple.com/newsroom/2026/02/the-biggest-hits-of-bad-bunnys-apple-music-super-bowl-lx-halftime-show/)
	- [Apple Sports adds golf to its lineup](https://www.apple.com/newsroom/2026/02/apple-sports-adds-golf-to-its-lineup/)
```

## Troubleshooting

- If you see authentication errors, confirm `GOOGLE_API_KEY` is correctly set and the Generative Language API is enabled for your project.
- If dependencies fail to install, confirm your Python version and that your virtual environment is active.
