import smtplib
import credentials
from email.mime.text import MIMEText
smtp_server=smtplib.SMTP('smtp.gmail.com : 587')
smtp_server.starttls()
email=credentials.email
password=credentials.password
smtp_server.login(email, password)
message=MIMEText("Hey , This is a bot")
message['From']=email
message['To']=email
message['Subject']='An automated email'

smtp_server.sendmail(email, email, message.as_string())
print("Success") 