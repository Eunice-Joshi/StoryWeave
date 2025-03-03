from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
@app.route('/')
def home():
    return "StoryWeave is Live! Use /generate to create a story."

CORS(app)

TOGETHER_AI_API_KEY = os.getenv("TOGETHER_AI_API_KEY")
TOGETHER_AI_MODEL = os.getenv("TOGETHER_AI_MODEL")

@app.route('/generate', methods=['POST'])
def generate_story():
    data = request.json
    user_prompt = data.get('prompt', 'Once upon a time...')

    api_url = "https://api.together.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_AI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": TOGETHER_AI_MODEL,
        "messages": [{"role": "user", "content": user_prompt}],
        "max_tokens": 1500
    }

    response = requests.post(api_url, json=payload, headers=headers)
    response_data = response.json()

    return jsonify({"story": response_data['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

