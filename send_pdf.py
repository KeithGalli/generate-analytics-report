import os
import smtplib
#import imghdr
from email.message import EmailMessage
from report import create_pdf

EMAIL_ADDRESS = "kgmit18@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

contacts = ['kgmit18@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Testing an email send'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'kgmit18@gmail.com'

msg.set_content('Attached is the analytics report form this week')

create_pdf()

with open('py3k.pdf', 'rb') as f:
  data = f.read()
  name = f.name

msg.add_attachment(data, filename=name, maintype='application/pdf', subtype='pdf')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
