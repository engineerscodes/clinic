from django.http.response import Http404
from patients.forms import Details_Form, NameForm, Report_Form
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Details
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def report(request):
    if request.method == 'POST':
        form = Report_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patients:report'))
    else:
        form = Report_Form()

    return render(request, 'patients/report.html', {
        'details': Details.objects.all(),
        'form': form
    })


def index(request):
    if request.method == 'POST':
        form = Details_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patients:index'))

    else:
        form = Details_Form()

    return render(request, 'patients/index.html', {'form': form})


def details(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'patients/details.html', {
        'details': Details.objects.all()
    })


def view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            return HttpResponseRedirect(reverse("patients:display", args=((number,))))
        else:
            raise Http404
    else:
        form = NameForm()

    return render(request, 'patients/view.html', {'form': form})


def display(request, number):
    return render(request, 'patients/display_detail.html',
                  {'patient': Details.objects.get(mobile=number)})
