# codigo comum compartilhado pelas apps
from enum import Enum, EnumMeta

default_app_config = "sgi.commons.apps.CommonsConfig"


class ChoiceEnumCharValueMeta(EnumMeta):
    def __iter__(self):
        return ((tag.value, tag.value) for tag in super().__iter__())


class AutoNameEnum(Enum):
    # pylint: disable=no-self-argument
    def _generate_next_value_(name, start, count, last_values):
        # pylint: disable=no-member
        return name.title()
