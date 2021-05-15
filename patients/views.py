from patients.forms import Details_Form
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Details
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        form = Details_Form(data=request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Details_Form()

    return render(request, 'patients/index.html', {'form': form})


def details(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'patients/display.html', {
        'details': Details.objects.all()
    })
