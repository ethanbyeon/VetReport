from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *
from .filters import *

def home(request):
    return render(request, 'home/index.html')


def login(request):
    return render(request, 'accounts/login.html')


def userPage(request):

    cases = Case.objects.all()

    context = {'cases': cases}
    return render(request, 'accounts/user.html', context)


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


def updateCase(request, pk):

    case = Case.objects.get(id=pk)
    form = CaseForm(request.POST or None, request.FILES or None, instance=case)

    if request.method == 'POST':
        form = CaseForm(request.POST or None, request.FILES or None, instance=case)
        if form.is_valid():
            form.save()
            return redirect('user_page')

    context = {'form': form}
    return render(request, 'accounts/case.html', context)


def deleteCase(request, pk):

    case = Case.objects.get(id=pk)

    if request.method == 'POST':
        case.delete()
        return redirect('user_page')
    
    context = {'case': case}
    return render(request, 'accounts/client.html', context)


def dashboard(request):

    cases = Case.objects.all()
    clients = Client.objects.all()

    caseFilter = CaseFilter(request.GET, queryset=cases)
    cases = caseFilter.qs

    context = {'cases': cases, 'clients': clients, 'caseFilter':caseFilter}
    return render(request, 'accounts/dashboard.html', context)