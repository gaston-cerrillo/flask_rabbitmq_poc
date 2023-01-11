import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from decouple import config


pop3server = config('pop3server')
username = config('username')
password = config('password')
mail = config('mail')


def send_mail(address, subject='noreply', message=''):
    # msg = EmailMessage()
    # msg.set_content(message)
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = mail
    msg['To'] = address
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        connection = smtplib.SMTP(pop3server, 25)
        connection.ehlo()
        connection.starttls(context=context)
        connection.ehlo()
        connection.login(username, password)
        connection.send_message(msg)
    except Exception as e:
        print(e)
