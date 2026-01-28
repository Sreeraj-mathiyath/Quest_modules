import smtplib
s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login('sraj617182@gmail.com','vsug kosr lwzb jgml')
msg="this is a testing mail"
s.sendmail('sraj617182@gmail.com','sreerajmathiyath6785@gmail.com',msg)
s.quit()