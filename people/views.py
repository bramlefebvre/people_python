from django.shortcuts import render
from django.http import HttpResponse
from people.models import Person
import json


# Create your views here.


def index(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    print("name: " + name)
    Person.objects
    serialized_persons = get_persons()
    persons_json = json.dumps(serialized_persons)
    return HttpResponse(persons_json)



def serialize_persons(persons):
    serialized_persons = []
    for person in persons:
        serialized_person = {
            'name': person.name,
            'age': person.age
        }
        serialized_persons.append(serialized_person)
    return serialized_persons

def get_persons():
    persons = Person.objects.all()
    persons = persons.iterator()
    serialized_persons = []
    for person in persons:
        serialized_person = {
            'name': person.name,
            'age': person.age
        }
        serialized_persons.append(serialized_person)
    return serialized_persons
    # return json.dumps(serialized_persons)

