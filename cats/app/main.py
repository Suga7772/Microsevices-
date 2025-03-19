from flask import Flask, send_file
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Cat Microservice - Access /cat for image!!"

@app.route('/cat')
def get_cat():
    try:
        # Get image from API
        response = requests.get('https://cataas.com/cat', stream=True)
        response.raise_for_status()
        
        # Return image with proper content type
        return send_file(
            response.raw,
            mimetype=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.exceptions.RequestException as e:
        return f"Error fetching cat image: {str(e)}", 500
    except Exception as e:
        return f"Unexpected error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)