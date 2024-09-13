from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'homeTMC/home.html')

def contato(request):
    return HttpResponse('CONTATO')

def agenda(request):
    return HttpResponse('AGENDA')