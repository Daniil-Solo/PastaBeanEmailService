import json

from src.events.base_event import BaseEvent
from src.utils.event_registry import EventRegistry


class EventExtractor:
    def __init__(self, registry: EventRegistry):
        self.__registry = registry

    def extract(self, json_string: str) -> BaseEvent:
        json_data = json.loads(json_string)
        event_type = json_data["type"]
        event_class = self.__registry.get(event_type)
        return event_class(**json_data)
