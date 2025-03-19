from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/joke', methods=['GET'])
def get_joke():
    try:
        response = requests.get('https://v2.jokeapi.dev/joke/Any?type=single', timeout=5)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch joke", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3006, debug=True)
