import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = '444447@gmail.com'
    msg['To'] = '4444444@gmail.com'

    with smtplib.SMTP('smpt.gmail.com', 587) as server:
        server.starttls()
        server.login('444444@gmail.com', '#3333')
        server.send_message(msg)

# Use this function to send alerts when Nmap or a suspicious scan is detected
send_alert("Nmap Detected!", "Nmap has been detected scanning 127.0.0.1.")

