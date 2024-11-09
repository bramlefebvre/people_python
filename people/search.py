from people.models import Person
import json


def search_person(name, age):
    if name is None and age is None:
        persons = Person.objects.all()
    else:
        if name is not None:
            persons = Person.objects.filter(name__icontains = name)
            if age is not None:
                persons = persons.filter(age = age)
        else:
            persons = Person.objects.filter(age = age)
    serialized_persons = serialize_persons(persons)
    persons_json = json.dumps(serialized_persons)
    return persons_json



def serialize_persons(persons):
    persons = persons.iterator()
    serialized_persons = []
    for person in persons:
        serialized_person = {
            'name': person.name,
            'age': person.age
        }
        serialized_persons.append(serialized_person)
    return serialized_persons
