from src.events.base_event import BaseEvent

REGISTER_EVENT_NAME = "register"
REGISTER_TEMPLATE_NAME = "register_email.html"


class RegisterEvent(BaseEvent):
    name: str
    activation_link: str
