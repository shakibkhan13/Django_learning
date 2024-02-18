from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Blogs(request):
    return HttpResponse("<h1>This is Video Blogs</h1>")