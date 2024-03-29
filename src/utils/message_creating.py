from email.message import EmailMessage
from pydantic import EmailStr


class EmailMessageCreator:
    def __init__(self, from_email: EmailStr):
        self.__from_email = from_email

    def create(self, to_email: EmailStr, subject: str, content: str) -> EmailMessage:
        message = EmailMessage()
        message["From"] = self.__from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(content, subtype='html')
        return message
