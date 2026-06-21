# weatherAI_apiInterview

A simple Flask weather proxy app that serves a static UI and forwards requests to the Weather AI API.

# Clone the repository and cd into it  

```
git clone https://github.com/KenNyagz/weatherAI_apiInterview.git
cd weatherAI_apiInterview.git
```

## Environment

This project uses a Python virtual environment and environment variables for configuration.

Create a `.env` file in the repository root with:

```env
WEATHER_AI_API_KEY=wai_....
WEATHER_AI_BASE_URL=https://weather-ai.co
WEATHER_AI_ENDPOINT_PATH=/v1/weather
```

If you want to keep `.env` out of source control, use the existing `.env.example` as a reference.

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you already have the app dependencies installed, ensure `gunicorn` is available in the environment.

## Run locally

```bash
source .venv/bin/activate
python app.py
```

Then visit `http://127.0.0.1:5000`.

## App structure

- `app.py` — main Flask app entrypoint used for local development and deployment.
- `templates/` — HTML templates for the web UI.
- `static/` — CSS and static assets.
