from django.urls import path

from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path("create", views.create, name="create")
]