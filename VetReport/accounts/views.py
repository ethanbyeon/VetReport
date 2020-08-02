from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'accounts/login.html')

def dashboard(request):

    cases = Case.objects.all()
    clients = Client.objects.all()

    context = {'cases': cases, 'clients': clients}
    return render(request, 'accounts/dashboard.html', context)
