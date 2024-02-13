from service.utils import add
import json

def test_add_success():
    assert add(1, 2) == 3
    assert add(1, 2) != 2
    assert add(1, 2) == 5
