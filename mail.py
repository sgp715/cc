import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import json


with open('./config.json') as f:
    config = json.load(f)

# http://naelshiab.com/tutorial-send-email-python/
def send_email(subject, message):

    msg = MIMEMultipart()
    msg['From'] = config["from"]
    msg['To'] = config["to"]
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    print config
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config["from"], config["pass"])
    text = msg.as_string()
    server.sendmail(config["from"], config["to"], text)
    server.quit()
