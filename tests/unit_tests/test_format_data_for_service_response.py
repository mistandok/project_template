from service.utils import Man, format_data_for_service_response
from tests.fixtures.repeatable_data import example_people


def test_format_data_for_service_response(example_people: list[Man]):
    assert format_data_for_service_response(example_people) == {
        1: "Artikov Anton",
        2: "Ivanov Ivan",
    }
