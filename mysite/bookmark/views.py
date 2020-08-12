from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

#index 함수를 만들자 
def index(request):
    return HttpResponse("Hello Django")

def test(request):
    msg = "This is Django Test"
    return HttpResponse(msg)
    
def myname(request):
    msg = "<h1>My name is Tom</h1>"
    return HttpResponse(msg)