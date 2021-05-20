from datetime import date

from django.contrib import messages
from django.http.response import Http404
from patients.forms import Details_Form, NameForm, Report_Form
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Details, Report
from DOCTORS.models import DOCTORS
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def report(request):
    if request.user.is_authenticated == False:
        return redirect('/')
    try:
        IS_doc = DOCTORS.objects.get(pk=request.user)
    except Exception as e:
        print("INVALID PERSON")
        IS_doc = None
    if IS_doc is None:
        return redirect('/')
    if request.method == 'POST' and IS_doc is not None:
        form = Report_Form(data=request.POST, files=request.FILES)
        if form.is_valid():

            new_form = form.save(commit=False)
            # print(request.POST['number'])
            # new_form.patient=request.POST['number'] -->Cannot assign "'6383128594'":
            # "Report.patient" must be a "Details" instance.
            try:

                numObj = Details.objects.get(mobile=request.POST['number'])
                if numObj.is_checked == True:
                    try:
                        doc = Report.objects.get(pk=numObj)
                        # print(doc)
                        messages.info(
                            request,
                            f"!!The Record Was Updated by {doc.doctor_name}  few seconds ago!!")
                        return redirect('/report/')
                    except Exception as e:
                        messages.info(request, f"!!Record Submitted!!")
                        numObj.is_checked = True
                        numObj.save()
                        new_form.patient = numObj
                        new_form.doctor_name = request.user.username
                        # request.user.email
                        new_form.client_name = numObj.name
                        new_form.save()
                        return redirect('/report/')

                else:
                    numObj.is_checked = True
                    numObj.save()
                    new_form.patient = numObj
                    new_form.doctor_name = request.user.username
                    # request.user.email
                    new_form.client_name = numObj.name
                    new_form.save()
                    messages.info(request, f"!!Record Submitted!!")

                    return HttpResponseRedirect(reverse('patients:report'))
            except Exception as e:
                print(e)

    else:
        form = Report_Form()

    return render(request, 'patients/report.html', {
        'details': Details.objects.filter(is_checked=False),
        'form': form
    })


def index(request):
    if request.method == 'POST':
        form = Details_Form(data=request.POST)
        if form.is_valid():

            new_form = form.save(commit=False)
            new_form.Form_date = date.today().strftime('%Y-%m-%d')

            new_form.save()
            messages.info(request, "FORM SUBMITTED ")
            return redirect('/')
        else:
            return render(request, 'patients/index.html', {'form': form})
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
