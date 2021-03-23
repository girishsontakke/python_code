import os
import smtplib
import imghdr
from email.message import EmailMessage

email = os.environ.get("EMAIL_USER")
password = os.environ.get("EMAIL_PASSWORD")
msg = EmailMessage()
msg['Subject'] = "no reply"
msg['From'] = email
msg['To'] = 'girishsontakke7@gmail.com'
msg.set_content("how are you")

with open("my_img.jpg", 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype="image",
                   subtype=file_type, filename=file_name)

# for pdf use maintype='application' subtype='octed-stream'


# port = 587 for SMTP AND  port = 465 for SMTP_SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, password)
    smtp.send_message(msg)
