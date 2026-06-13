from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SUBSCRIPTION_KEY = os.getenv("TRANSLATOR_KEY")
REGION = os.getenv("TRANSLATOR_REGION")
ENDPOINT = os.getenv("TRANSLATOR_ENDPOINT")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")
    source_lang = data.get("source")
    target_lang = data.get("target")

    url = f"{ENDPOINT}/translate?api-version=3.0&from={source_lang}&to={target_lang}"
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
        "Ocp-Apim-Subscription-Region": REGION,
        "Content-Type": "application/json"
    }
    body = [{"Text": text}]

    response = requests.post(url, headers=headers, json=body)
    result = response.json()
    translated_text = result[0]["translations"][0]["text"]

    return jsonify({"translated": translated_text})

import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)