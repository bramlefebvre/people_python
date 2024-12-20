from dataclasses import dataclass
from people.models import Person
from enum import Enum, unique
from django.db import utils
import logging
import traceback

def create_person(person_dict):
    person = deserialize_person(person_dict)
    if person.age < 18:
        return Response(Status.NO_SUCCESS, "age_must_be_18_or_higher")
    try:
        person.save()
    except utils.IntegrityError as e:
        logging.debug(traceback.format_exc())
        return Response(Status.NO_SUCCESS, "name_already_exists")
    return Response(Status.SUCCESS, "success")

def deserialize_person(person_dict):
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
    message_code: str


