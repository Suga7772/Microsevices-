from flask import Flask, request
import smtplib, os

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    # using secrets to hide the username and passwork for the email type.
    smtp_user = os.environ.get('SMTP_USER')
    smtp_pass = os.environ.get('SMTP_PASS')
    
    msg = "Subject: Test Email\n\nThis is a dummy email from Flask Microservice."
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, 'receiver@email.com', msg)
    return 'Email sent', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)