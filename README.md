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
cp .env.example .env
```
Remember to substitute the corret API key

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

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

Live deployment: https://weather-a-iapi-interview--kennyagz681.replit.app
