import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASSWORD = "your_app_password"

msg = MIMEText("Hello, this is a test mail!")
msg['Subject'] = "Test"
msg['From'] = SENDER_EMAIL
msg['To'] = "receiver@gmail.com"

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")