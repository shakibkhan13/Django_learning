from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Data_Analysis(request):
    return HttpResponse("<h1>It is a Data Analysis</h1>")