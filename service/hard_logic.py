import dataclasses

import requests


@dataclasses.dataclass(frozen=True)
class Student:
    name: str
    surname: str
    group: int


@dataclasses.dataclass(frozen=True)
class Professor:
    id: int
    name: str
    surname: str
    skills: list[str]

    def __hash__(self):
        return self.id


class UniversityClient:
    def __init__(self, url: str):
        self._url = url

    def get_students(self) -> list[Student]:
        pass

    def get_professors(self) -> list[Professor]:
        pass


class RemoteServerError(Exception):
    pass


class Worker:
    def __init__(self, university_client: UniversityClient):
        self._university_client = university_client

    def distribute_students_among_professors(self) -> dict[Professor, list[Student]]:
        try:
            students = self._university_client.get_students()
            professors = self._university_client.get_professors()
        except requests.Timeout:
            raise RemoteServerError

        beginner_professors_for_students = {}
        smart_professors_for_students = {}

        for professor in professors:
            if is_very_smart_professor(professor):
                smart_professors_for_students[professor] = []
            else:
                beginner_professors_for_students[professor] = []

        for student in students:
            if is_even_group(student.group):
                for professor in smart_professors_for_students.keys():
                    smart_professors_for_students[professor].append(student)
            else:
                for professor in beginner_professors_for_students.keys():
                    beginner_professors_for_students[professor].append(student)

        return {**beginner_professors_for_students, **smart_professors_for_students}


def is_even_group(group: int):
    return group % 2 == 0


def is_very_smart_professor(professor: Professor):
    return len(professor.skills) > 2


