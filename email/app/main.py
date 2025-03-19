from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    msg = "Subject: Test Email\n\nThis is a dummy email from my aws assignment of 3 Microservice."
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('mahrukhkhan702@gmail.com', 'IDLNBHLMIOLr7*')
        server.sendmail('mahrukhkhan702@gmail.com', 'viyonmk7@gmail.com', msg)
    return 'Email sent', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)