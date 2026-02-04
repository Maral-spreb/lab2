from django.shortcuts import render
from django.http import HttpResponse

def poll(request):
    return HttpResponse ("<h3>Hello Poll App</h3>")

# Create your views here.
