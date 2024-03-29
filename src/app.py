import json

from src.config import app_config
from src.events.register_event import REGISTER_EVENT_NAME, REGISTER_TEMPLATE_NAME, RegisterEvent
from src.service import EmailService
from src.utils.event_extraction import EventExtractor
from src.utils.event_registry import EventRegistry
from src.utils.message_creating import EmailMessageCreator
from src.utils.sending import EmailMessageSender
from src.utils.template_registry import TemplateRegistry
from src.utils.template_rendering import TemplateRender


if __name__ == '__main__':
    data = RegisterEvent(
        name="John", activation_link="http://pastabean", type=REGISTER_EVENT_NAME,
        email=app_config.SERVICE_EMAIL, subject="Finish registration"
    )
    json_string = json.dumps(data.model_dump())
    event_registry = (
        EventRegistry()
        .set(REGISTER_EVENT_NAME, RegisterEvent)
    )
    extractor = EventExtractor(event_registry)
    template_registry = (
        TemplateRegistry()
        .set(REGISTER_EVENT_NAME, REGISTER_TEMPLATE_NAME)
    )
    template_render = TemplateRender(template_registry, 'src', 'templates')
    email_creator = EmailMessageCreator(app_config.SERVICE_EMAIL)
    sender = EmailMessageSender(app_config.SERVICE_EMAIL, app_config.SERVICE_PASSWORD, app_config.SMTP_HOST, app_config.SMTP_PORT)
    service = EmailService(extractor, template_render, email_creator, sender)
    service.handle(json_string)
