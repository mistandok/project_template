from service.utils import add


def test_add_success():
    assert add(1, 2) == 3
    assert add(1, 2) != 2
    assert add(1, 10) == 11
