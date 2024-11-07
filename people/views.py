from django.shortcuts import render
from django.http import HttpResponse
from people.search import search_person
from people.create import create_person
# import json


# Create your views here.


def search(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    persons_json = search_person(name, age)
    return HttpResponse(persons_json)


def create(request):
    create_person(request.body)

