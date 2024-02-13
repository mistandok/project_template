import dataclasses
import json
from curses.ascii import isalpha
from typing import Iterable


@dataclasses.dataclass
class Man:
    name: str
    surname: str


def add(x: int, y: int) -> int:
    return x + y


class WrongDivider(Exception):
    pass


def division(x: int, y: int) -> int:
    if y == 0:
        raise WrongDivider
    return x // y


def is_palindrome(text: str):
    # return text.lower() == "".join(reversed(text.lower()))
    formatted_text = "".join(ch for ch in text.lower() if ch.isalpha())
    return formatted_text == "".join(reversed(formatted_text))


def format_data_for_display(people: list[Man]) -> list[str]:
    return list(f"Cool man: {man.surname} {man.name}" for man in people)


def format_data_for_service_response(people: list[Man]) -> dict:
    return {man_id: f"{man.surname} {man.name}" for man_id, man in enumerate(people, start=1)}
