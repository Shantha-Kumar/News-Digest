import ssl, smtplib
import os
def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    username = "shand.luffy@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "shand.luffy@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
