from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("todos/" , views.todos, name="todos")
]