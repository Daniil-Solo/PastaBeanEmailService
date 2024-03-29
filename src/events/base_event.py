from pydantic import BaseModel, EmailStr


class BaseEvent(BaseModel):
    type: str
    email: EmailStr
    subject: str
