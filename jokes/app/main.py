from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/joke')
def get_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)