import sqlite3

import pytest

from settings import DB_NAME


@pytest.fixture(scope="session", autouse=True)
def sqlite_connection():
    connection = sqlite3.connect(DB_NAME)
    yield connection
    connection.close()
