#--------------------------sending mail using python------------------------
import smtplib
from email.message import EmailMessage


sender = "manasagongolla3@gmail.com"
receiver = "rakkeshadithya00@gmail.com"
password = "jhyevhgjaeypjoni"

message=EmailMessage()
message['From'] = sender
message['To'] = (receiver)
message['Subject']="Python email project"

message.set_content=("hii")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(sender, password)
    connection.send_message(message)

print('Email sent sucessfully')

