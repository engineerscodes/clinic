from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.models import  auth,User
from django.contrib import messages
from django.views import View
from patients.models import Details,Report
from .Token_Gen import Token_generator
from django.core.mail import send_mail

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from django.http import HttpResponse

from django.template.loader import  render_to_string

from django.utils.encoding import  force_text,force_bytes,  DjangoUnicodeDecodeError

from django.contrib.sites.shortcuts import get_current_site


import threading


class THREADEMAIL(threading.Thread):
    def __init__(self, message, email):
        self.message = message
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
            send_mail(
                'THANKS FOR REG',
                self.message,
                'naveennoob95@gmail.com',
                [self.email],
                fail_silently=False,

            )



def index(request):
    if  request.user.is_authenticated ==False:
        #return HttpResponseRedirect(reverse('users:login'))
        return redirect('/users/login/')
    totalrec=Details.objects.all().count()
    totalpen=Report.objects.all().count()
    userREC=Report.objects.filter(doctor_name=request.user.username).count()
    return render(request, 'users/user.html',{'counts':totalrec,'pen':totalpen,'rec':userREC})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'users/login.html', {
                'message': "Invalid credentials"
            })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        "message": 'Logged out!'
    })


def reg(request):
    if request.method == 'GET':
        return render(request, 'users/reg.html')
    if request.method == 'POST':

        userName = request.POST['names']
        password = request.POST['password_cfn']
        email = request.POST['emails']

        if User.objects.filter(username=userName).exists():
            messages.info(request, " UserName is not Available")
            return redirect('/users/reg/')
        if User.objects.filter(email=email).exists():
            messages.info(request, " MAIL IS ALREADY REG")
            return redirect('/users/reg/')

        if  User.objects.filter(username=userName).exists() == False:
            user = User.objects.create_user(username=userName, password=password, email=email)
            user.is_active = False
            user.save()
            # PasswordResetTokenGenerator use it to verfiy and create token also
            Useract_token = Token_generator()

            message = render_to_string('users/activate.html',
                                       {
                                           'user': user,
                                           'domain': get_current_site(request),
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'TOKEN': Useract_token.make_token(user)

                                       }
                                       )
            ''' send_mail(
                               'THANKS FOR REG',
                               message,
                               'naveennoob95@gmail.com',
                               [email],
                               fail_silently=False,
            )'''

            THREADEMAIL(message, email).start()

            messages.info(request, " plz verfiy your email ")
            return redirect('/users/reg/')


def AUTHUSERNAME(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    Useract_token = Token_generator()
    if user is not None and Useract_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.info(request, "VALIDATED USER PLZ LOGIN ")

        return redirect('/users/login/')

    return render(request, 'users/errorlogin.html', status=401)
