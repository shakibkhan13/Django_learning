"""
URL configuration for jano project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from jano import Blogs, Data_Analysis, Deep_learning, machine_learning
# from machine_learning import views as m
# from Blogs import views as B
# from Data_Analysis import views as D
# from Deep_learning import views as DP


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Ml',include(machine_learning.urls)),
    path('Blogs/',include(Blogs.urls)),
    path('Data/',include(Data_Analysis.urls)),
    path('Deep/',include(Deep_learning.urls))
    
    # path('',m.machine_learning),
    # path('b/',B.Blogs),
    # path('D/',D.Data_Analysis),
    # path('p/',DP.Deep_learning)
]
