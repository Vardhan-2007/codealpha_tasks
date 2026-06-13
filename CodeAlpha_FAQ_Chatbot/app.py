import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from flask import Flask, request, jsonify, render_template
from matcher import FAQMatcher

app = Flask(__name__)

# Load the matcher once when server starts
# This preprocesses all FAQs and builds the TF-IDF matrix at startup
matcher = FAQMatcher()

# Route 1 — serves your chatbot.html when you visit localhost:5000
@app.route("/")
def home():
    return render_template("chatbot.html")

# Route 2 — receives user question, returns bot answer as JSON
@app.route("/ask", methods=["POST"])
def ask():
    data       = request.get_json()
    user_input = data.get("question", "").strip()

    if not user_input:
        return jsonify({ "answer": "Please type a question!" })

    result = matcher.get_answer(user_input)
    return jsonify({ "answer": result })

import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)