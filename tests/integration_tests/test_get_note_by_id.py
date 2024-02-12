import sqlite3

import pytest

from service.db import get_note_by_id, DataNotFound, Note
from tests.fixtures.connections import sqlite_connection


def test_get_note_by_id_data_not_found(sqlite_connection: sqlite3.Connection):
    with pytest.raises(DataNotFound):
        get_note_by_id(sqlite_connection, 10)


def test_get_note_by_id_data_success(sqlite_connection: sqlite3.Connection):
    assert get_note_by_id(sqlite_connection, 1) == Note(id=1, description="note_1")
