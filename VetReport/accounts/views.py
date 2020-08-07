from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

def home(request):
    return render(request, 'home/index.html')


def login(request):
    return render(request, 'accounts/login.html')


def userPage(request):
    return render(request, 'accounts/client.html')


def createCase(request):
    form = CaseForm()
    
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            case = form.save(commit=False)
            case.profile = request.user.profile

            case.save()

            return redirect('user_page')
    
    context = {'form': form}
    return render(request, 'accounts/case.html', context)


def dashboard(request):

    cases = Case.objects.all()
    clients = Client.objects.all()

    context = {'cases': cases, 'clients': clients}
    return render(request, 'accounts/dashboard.html', context)
