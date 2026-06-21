import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

base_dir = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(base_dir, '.env'))

app = Flask(__name__, template_folder='templates')
BASE_URL = os.getenv('WEATHER_AI_BASE_URL', 'https://weather-ai.co')
ENDPOINT_PATH = os.getenv('WEATHER_AI_ENDPOINT_PATH', '/v1/weather')
API_KEY = os.getenv('WEATHER_AI_API_KEY', '')

print(f"Loaded configuration: BASE_URL={BASE_URL}, ENDPOINT_PATH={ENDPOINT_PATH}, API_KEY={API_KEY}")

def build_target_url(params):
    query = params.to_dict(flat=True)
    base = BASE_URL.rstrip('/')
    path = ENDPOINT_PATH
    if query:
        return f"{base}{path}?{requests.compat.urlencode(query)}"
    return f"{base}{path}"


@app.route('/')
def home():
    return render_template(
        'index.html',
        page_title='WeatherAI Landing',
        header='WeatherAI Explorer',
        description='Search weather forecasts using Weather-AI and preview the JSON response right from this page.',
        default_location='Nairobi',
        default_units='metric',
    )


@app.route('/v1/weather')
def weather():
    if not request.args:
        return jsonify({'error': 'Please provide query parameters, e.g. location=Nairobi'}), 400

    try:
        target_url = build_target_url(request.args)
        headers = {'Authorization': f'Bearer {API_KEY}'} if API_KEY else {}
        response = requests.get(target_url, headers=headers, timeout=10)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as exc:
        return jsonify({'error': str(exc)}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
