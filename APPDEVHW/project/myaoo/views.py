from django.shortcuts import render, HttpResponse
from .models import TodoList

# Create your views here.
def home(request):
    return render(request, "home.html")

def contacts(request):
    return render(request, "contacts.html")

def aboutus(request):
    return render(request, "aboutus.html")
    
def todos(request):
    items = TodoList.objects.all()
    return render(request, "todos.html", {"todos": items})
