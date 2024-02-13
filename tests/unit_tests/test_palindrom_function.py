from time import sleep

import pytest

from service.utils import is_palindrome

"""
Пример парамтеризованных тестов.
Хорошей практикой можно считать разделение тестов по различному поведению:
В примерах ниже это разделение на test_is_palindrome и test_is_palindrome_is_not_palindrome.
Такие тесты понятнее и проще читать.
Пример test_is_palindrome с ожидаемым результатом читается сложнеие,
потому что в нем тестируются два различных поведения.
"""


@pytest.mark.parametrize(
    "text",
    [
        "",
        "a",
        "Bob",
        "never odd or even",
        "Do geese see God?",
    ],
)
def test_is_palindrome(text: str):
    assert is_palindrome(text)


@pytest.mark.parametrize(
    "text",
    [
        "lala",
        "abc",
    ],
)
def test_is_palindrome_is_not_palindrome(text: str):
    assert not is_palindrome(text)


@pytest.mark.parametrize(
    "text, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(text: str, expected_result: bool):
    assert is_palindrome(text) == expected_result


# категоризация тестов
@pytest.mark.slow
def test_big_is_palindrome():
    text = "bob"
    sleep(5)
    assert is_palindrome(text)
