import smtplib      #Connects to SMTP server to send email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "sraj617182@gmail.com"
password = "vsug kosr lwzb jgml"
receiver = "sreerajmathiyath6785@gmail.com"

msg = MIMEMultipart()
msg['From']=sender
msg['To']=receiver
msg['Subject']='Test email with attachment'

body = "Hello,\nThis email contains an attachment.\nRegards,\nPython Script"
msg.attach(MIMEText(body,'plain'))

file_path = r"D:\Quest\assignments.zip"
file_name = 'assignments.zip'

try:
    with open(file_path,'rb') as attachment:
        mime = MIMEBase("application","octet-stream")
        mime.set_payload(attachment.read())
        encoders.encode_base64(mime)
        mime.add_header("Content-Disposition",f"attachment; filename={file_name}")
        msg.attach(mime)
except Exception as e:
    print(f"An Exception occured {e}")
try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender,password)
        server.send_message(msg)
    print("Message sent successfully")
except Exception as e:
    print("an exception occured")
