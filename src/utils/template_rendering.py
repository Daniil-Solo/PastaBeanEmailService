from jinja2 import Environment, PackageLoader

from src.utils.template_registry import TemplateRegistry


class TemplateRender:
    def __init__(self, template_registry: TemplateRegistry, package_name: str, package_path: str):
        self.__env = Environment(
            loader=PackageLoader(package_name, package_path)
        )
        self.__template_registry = template_registry

    def render(self, event_type: str, data: dict):
        template_name = self.__template_registry.get(event_type)
        template = self.__env.get_template(template_name)
        content = template.render(**data)
        return content
