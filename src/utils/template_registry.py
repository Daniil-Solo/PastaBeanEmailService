from src.exceptions import UnknownEventTypeError


class TemplateRegistry:
    def __init__(self):
        self.__data = dict()

    def set(self, key: str, template: str) -> "TemplateRegistry":
        self.__data[key] = template
        return self

    def get(self, key: str) -> str:
        if key not in self.__data:
            raise UnknownEventTypeError(f"No registered template for event type {key}")
        return self.__data[key]
