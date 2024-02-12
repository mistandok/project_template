import pytest

from service.hard_logic import Student, Professor
from service.utils import Man


@pytest.fixture
def example_people() -> list[Man]:
    return [
        Man(name="Anton", surname="Artikov"),
        Man(name="Ivan", surname="Ivanov"),
    ]


@pytest.fixture
def students() -> list[Student]:
    return [
        Student("Anton", "Artikov", 1),
        Student("Ivan", "Ivanov", 2),
        Student("Dima", "Petrov", 3),
        Student("Nastya", "Ivanova", 4),
        Student("Katya", "Bulgakova", 5),
    ]


@pytest.fixture
def professors() -> list[Professor]:
    return [
        Professor(1, "Albert", "Einstein", ["physics", "mathematics", "probability theory"]),
        Professor(2, "Mikhail", "Lomonosov", ["astronomy", "physics", "chemistry"]),
        Professor(3, "Vasya", "Pupkin", ["good man"])
    ]
