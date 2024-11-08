import json
from people.models import Person
from enum import Enum, unique

def create_person(person_json):
    person = deserialize_person(person_json)
    print("person:" + str(person))
    if person.age < 18:
        return Status.NO_SUCCESS
    person.save()
    return Status.SUCCESS

def deserialize_person(person_json):
    person_dict = json.loads(person_json)
    name = person_dict['name']
    age = person_dict['age']
    person = Person(name = name, age = age)
    return person

@unique
class Status(Enum):
    SUCCESS = 1
    NO_SUCCESS = 2
