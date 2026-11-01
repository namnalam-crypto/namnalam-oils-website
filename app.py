import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Search keyword intents for marketing
TRENDING_KEYWORDS = [
    "best organic cold pressed coconut oil brand",
    "pure wood pressed groundnut oil price 1L",
    "traditional chekku gingelly oil online delivery"
]

@app.route('/')
def home():
    return render_template('index.html', keywords=TRENDING_KEYWORDS)

@app.route('/health')
def health_check():
    """Endpoint used by Render cron job to keep the site active"""
    return jsonify({"status": "active", "message": "Namnalam oils website is live!"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
