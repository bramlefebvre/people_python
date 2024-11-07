from django.shortcuts import render
from django.http import HttpResponse
from people.search import search_person
from people.create import create_person
from django.views.decorators.csrf import csrf_exempt
# import json


# Create your views here.


def search(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    persons_json = search_person(name, age)
    return HttpResponse(persons_json)

@csrf_exempt
def create(request):
    status = create_person(request.body)
    return HttpResponse()

