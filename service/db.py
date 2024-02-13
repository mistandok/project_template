import contextlib
import dataclasses
import sqlite3
from typing import Iterator

from settings import DB_NAME


@contextlib.contextmanager
def sqlite_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DB_NAME)
    yield connection
    connection.close()


def init_db(connection: sqlite3.Connection):
    connection.execute(
        """
    CREATE TABLE IF NOT EXISTS note (
        id INTEGER PRIMARY KEY,
        description TEXT
    )
    """
    )

    connection.execute(
        """
    INSERT INTO note (id, description)
    VALUES
        (1, 'note_1'),
        (2, 'note_2'),
        (3, 'note_2'),
        (4, 'note_4')
    """
    )

    connection.commit()


@dataclasses.dataclass
class Note:
    id: int
    description: str


class DataNotFound(Exception):
    pass


def get_note_by_id(connection: sqlite3.Connection, note_id: int) -> Note:
    cursor = connection.cursor()
    cursor.execute("""SELECT id, description FROM note WHERE id = ?""", [note_id])
    result = cursor.fetchone()
    if not result:
        raise DataNotFound

    return Note(*result)


if __name__ == "__main__":
    need_init = False
    with sqlite_connection() as conn:
        if need_init:
            init_db(conn)
        note = get_note_by_id(conn, 1)
        print(note)
