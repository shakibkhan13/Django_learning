from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    return HttpResponse('<h1>Hi ! , This is Machine Learning</h1>')