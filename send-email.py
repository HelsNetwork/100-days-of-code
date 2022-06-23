import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()


with open("password.txt", "r") as f:
    password = f.read()

server.login("SENDER", password)

msg = MIMEMultipart()
msg["From"] = "NAME"
msg["To"] = "RECIVER"
msg["Subject"] = "SUBJECT"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

filename = "IMAGE.JPG"
attachment = open(filename, "rb")

p = MIMEBase("application", "octect-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Dispostion", f"attachment; filename={filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail("SENDER", "RECIEVER", text)
