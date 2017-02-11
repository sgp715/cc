import smtplib
import json


with open('./config.json') as f:
    config = json.load(f)

# http://naelshiab.com/tutorial-send-email-python/
def send_email(message, to):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config["from"], config["pass"])
    server.sendmail(config["from"], to, message)
    server.quit()
