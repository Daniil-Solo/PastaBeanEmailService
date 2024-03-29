from src.events.base_event import BaseEvent
from src.exceptions import UnknownEventTypeError


class EventRegistry:
    def __init__(self):
        self.__data = dict()

    def set(self, key: str, data: type[BaseEvent]) -> "EventRegistry":
        self.__data[key] = data
        return self

    def get(self, key: str) -> type[BaseEvent]:
        if key not in self.__data:
            raise UnknownEventTypeError(f"No registered event for event type {key}")
        return self.__data[key]
