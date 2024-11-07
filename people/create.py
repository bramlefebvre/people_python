import json
from people.models import Person
from enum import Enum, unique

def create_person(serialized_person):
    person = json.loads(serialized_person)
    if person.age < 18:
        return Status.NO_SUCCESS
    Person.objects.create(person)


@unique
class Status(Enum):
    SUCCESS = 1
    NO_SUCCESS = 2
