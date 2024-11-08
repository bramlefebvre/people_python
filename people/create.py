from dataclasses import dataclass
import json
from people.models import Person
from enum import Enum, unique
from django.db import utils
import logging
import traceback

def create_person(person_json):
    person = deserialize_person(person_json)
    print("person:" + str(person))
    if person.age < 18:
        return Response(Status.NO_SUCCESS, "age must be 18 or higher")
    try:
        person.save()
    except utils.IntegrityError as e:
        logging.debug(traceback.format_exc())
        return Response(Status.NO_SUCCESS, "name already exists")
    return Response(Status.SUCCESS, "success")

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

@dataclass(frozen=True)
class Response:
    status: Status
    message: str


