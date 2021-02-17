import smtplib, ssl
from controllers.usersController import getUsersMail
from config import SMTPCONFIG

def send_message(data, user_id):
    context = ssl.create_default_context()

    sender = SMTPCONFIG["email"]
    receivers = getUsersMail(user_id)
    content = ""
    for field in data:
        content+="{name} set {value}\n".format(name=field, value=data[field])
    message = """\
Subject: Changes

Changes in:
{}
""".format(content)
    with smtplib.SMTP_SSL("smtp.gmail.com", SMTPCONFIG["port"], context=context) as server:
        server.login(SMTPCONFIG["email"], SMTPCONFIG["password"])
        server.sendmail(sender_email, receiver_email, message)