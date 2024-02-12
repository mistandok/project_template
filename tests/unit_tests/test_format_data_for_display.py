from service.utils import Man, format_data_for_display
from tests.fixtures.repeatable_data import example_people


def test_format_data_for_display(example_people: list[Man]):
    assert format_data_for_display(example_people) == [
        "Cool man: Artikov Anton",
        "Cool man: Ivanov Ivan",
    ]
