from django.shortcuts import render
from django.http import HttpResponse

def sayhello(request):
    return HttpResponse("Hello, world.") # pyright: ignore

def homepage(request):
    return render(request, "index.html")

