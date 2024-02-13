import mock
import pytest
import requests

from service.hard_logic import UniversityClient, RemoteServerError, Worker, Student, Professor
from tests.fixtures.repeatable_data import students, professors


def test_worker_client_get_professors_timeout(students: list[Student]):
    university_client = mock.create_autospec(UniversityClient, instance=True)
    university_client.get_students = mock.MagicMock(return_value=students)
    university_client.get_professors = mock.MagicMock(side_effect=requests.Timeout)

    worker = Worker(university_client)

    with pytest.raises(RemoteServerError):
        worker.distribute_students_among_professors()

    university_client.get_students.assert_called_once()
    university_client.get_professors.assert_called_once()


def test_worker_client_get_students_timeout(professors: list[Professor]):
    university_client = mock.create_autospec(UniversityClient, instance=True)
    university_client.get_students = mock.MagicMock(side_effect=requests.Timeout)
    university_client.get_professors = mock.MagicMock(return_value=professors)

    worker = Worker(university_client)

    with pytest.raises(RemoteServerError):
        worker.distribute_students_among_professors()


def test_worker_client_empty_result():
    university_client = mock.create_autospec(UniversityClient, instance=True)
    university_client.get_students = mock.MagicMock(return_value=[])
    university_client.get_professors = mock.MagicMock(return_value=[])
    expected_result = {}

    worker = Worker(university_client)
    result = worker.distribute_students_among_professors()

    university_client.get_students.assert_called_once()
    university_client.get_professors.assert_called_once()
    assert result == expected_result


def test_worker_client_success(students: list[Student], professors: list[Professor]):
    university_client = mock.create_autospec(UniversityClient, instance=True)
    university_client.get_students = mock.MagicMock(return_value=students)
    university_client.get_professors = mock.MagicMock(return_value=professors)

    expected_result = {
        Professor(1, "Albert", "Einstein", ["physics", "mathematics", "probability theory"]): [
            Student("Ivan", "Ivanov", 2),
            Student("Nastya", "Ivanova", 4),
        ],
        Professor(2, "Mikhail", "Lomonosov", ["astronomy", "physics", "chemistry"]): [
            Student("Ivan", "Ivanov", 2),
            Student("Nastya", "Ivanova", 4),
        ],
        Professor(3, "Vasya", "Pupkin", ["good man"]): [
            Student("Anton", "Artikov", 1),
            Student("Dima", "Petrov", 3),
            Student("Katya", "Bulgakova", 5),
        ],
    }

    worker = Worker(university_client)
    result = worker.distribute_students_among_professors()

    assert result == expected_result
