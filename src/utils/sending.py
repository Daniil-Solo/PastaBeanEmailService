import smtplib
import ssl
from email.message import EmailMessage

from pydantic import EmailStr


class EmailMessageSender:
    def __init__(self, from_email: EmailStr, password: str, smtp_host: str, smtp_port):
        self.__from_email = from_email
        self.__password = password
        self.__smtp_host = smtp_host
        self.__smtp_port = smtp_port

    def send(self, message: EmailMessage) -> None:
        to_email = message["To"]
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_host, self.__smtp_port, context=context) as smtp:
            smtp.login(self.__from_email, self.__password)
            smtp.sendmail(self.__from_email, to_email, message.as_string())
