import os
import smtplib
from pytz import timezone
from datetime import datetime, timedelta
from email.message import EmailMessage
from generate_report_simple import create_analytics_report

def lambda_handler(event, context):
    path = "" # insert your own path here

    EMAIL_ADDRESS = "kgmit18@gmail.com"
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = 'Covid-19 Analytics Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'kgmit18@gmail.com'

    msg.set_content('Attached is the analytics report form this week')

    yesterday = (datetime.now(timezone('US/Eastern')) - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
    create_analytics_report(yesterday, filename=f"{path}/tmp/report.pdf")

    with open(f'{path}/tmp/report.pdf', 'rb') as f:
      data = f.read()

    msg.add_attachment(data, filename='report.pdf', maintype='application/pdf', subtype='pdf')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)