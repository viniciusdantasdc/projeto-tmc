from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from homeTMC.views import home

urlpatterns = [
    path('', home), # HOME

]

# video 23 - movendo urls para views