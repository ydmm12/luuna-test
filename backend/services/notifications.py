import smtplib

def send_message(message_type, product):

    sender = 'ydmm12.dvt@gmail.com'
    receivers = ['yamil_David@hotmail.com']
    message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
send_message(1,2)