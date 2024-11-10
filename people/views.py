from django.shortcuts import render
from django.http import HttpResponse
from people.search import search_person
from people.create import Status, create_person
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def search(request):
    if request.method != "GET":
        return HttpResponse(status = 404)
    name = request.GET.get("name")
    age = request.GET.get("age")
    serialized_persons = search_person(name, age)
    persons_json = json.dumps(serialized_persons)
    return HttpResponse(persons_json)



@csrf_exempt
def create(request):
    if request.method != "POST":
        return HttpResponse(status = 404)
    person = json.loads(request.body)
    response = create_person(person)
    return to_HttpResponse(response)

def to_HttpResponse(response):
    if response.status == Status.SUCCESS:
        return HttpResponse(status=201)
    body = {
        'message_code': response.message_code
    }
    body = json.dumps(body)
    return HttpResponse(status=400, content=body)
