from django.urls import path
from . import views

urlpatterns = [
    path('m/',views.machine_learning)
]
