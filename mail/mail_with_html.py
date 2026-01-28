import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender = "sraj617182@gmail.com"
password = "vsug kosr lwzb jgml"
receiver = "sreerajmathiyath6785@gmail.com"

msg = MIMEMultipart()
msg['From']=sender
msg['To']=receiver
msg['Subject']='HTML Email Test'

html="""
<html>
  <body>
    <h2 style="color:blue;">Hello Sreeraj!</h2>
    <p>This is an <b>HTML email</b> sent using Python.</p>
    <p>Now you can use colors, layouts, buttons, and styles 🎉.</p>
    <a href="https://www.google.com" 
       style="background:green; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">
       Visit Google
    </a>
  </body>
</html>
"""


msg.attach(MIMEText(html,"html"))

try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender,password)
        server.send_message(msg)
    print("message sent successfully")

except Exception as e:
    print(f"Exception ocuured {e}")

