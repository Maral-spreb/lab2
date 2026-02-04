from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ("Hello News Site ")

# Create your views here.
