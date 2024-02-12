import pytest

from service.utils import division, WrongDivider


def test_division_success():
    assert division(8, 4) == 2
    assert division(10, 2) == 5


# Тест, проверяющий корректность выброса ошибок
def test_division_with_zero_divider():
    with pytest.raises(WrongDivider):
        division(10, 0)
