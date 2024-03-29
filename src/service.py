from src.utils.event_extraction import EventExtractor
from src.utils.message_creating import EmailMessageCreator
from src.utils.sending import EmailMessageSender
from src.utils.template_rendering import TemplateRender


class EmailService:
    def __init__(self, extractor: EventExtractor, template_render: TemplateRender, email_creator: EmailMessageCreator, sender: EmailMessageSender):
        self.__extractor = extractor
        self.__template_render = template_render
        self.__email_creator = email_creator
        self.__sender = sender

    def handle(self, json_string: str) -> None:
        current_event = self.__extractor.extract(json_string)
        content = self.__template_render.render(current_event.type, current_event.model_dump())
        message = self.__email_creator.create(current_event.email, current_event.subject, content)
        self.__sender.send(message)
