from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from homeTMC.views import home, agenda, contato

urlpatterns = [
    path('', home), # HOME
    path('agenda/', agenda), # /agenda/
    path('contato/', contato), # /contato/
]

# video 23 - movendo urls para views