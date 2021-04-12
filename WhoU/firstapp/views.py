from django.shortcuts import render, redirect
from .forms import UserForm
import pyrebase
from requests.exceptions import HTTPError
from django.core.signing import Signer
from datetime import timedelta
from django.core.signing import TimestampSigner
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
global Info
global Id
from .testfunctions import *
from .functions.getUser import *
from .functions.postsignin import *
from .functions.postsignup import *
from .functions.postimg import *
from .functions.postVK import *
from .functions.postprofile import *
import time



def index_profile(request):
    # try:
        userData = getUser(request)
        context = {
            'user': request.session.get('user_id'),
            'data': userData
        }
        if request.method == "POST":
            if request.POST.get('name') is not None:
                postprofile(request, context)
                if request.POST.get('isVk') == '1':
                    postVK(context)
            if request.FILES.get('image'):
                t = time.time()*1000
                file = request.FILES['image']
                postimg(file,context)
                print("\n\n\n\n ПОльзователь изминил фото \n\n\n\n")
            return redirect('/profile/')

        return render(request, "whou_profile.html", context)
    # except:
    #     return redirect('/')


def index_stat(request):
    context = {
        'user': request.session.get('user_id')
    }
    return render(request, "whou_statistics.html",context)


def send_mail(mail):
    import smtplib
    import random
    number = random.randint( 100000, 999999 )
    server = smtplib.SMTP( 'smtp.gmail.com', 587 )
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login( 'whoyouappp@gmail.com', 'Suslick228' )
    subject = 'verification code'
    body = 'verification code'
    message = "Your code - " + str(number)

    server.sendmail( 'whoyouappp@gmail.com', mail, message )
    server.quit()
    return number

def index_meetings(request):
    r = getUser(request, 2)
    context = {
        'user': request.session.get('user_id'),
    }
    if r != context['user']:
        context['lis'] = r
    return render(request, "whou_meetings.html", context)

def index_check(request):
    context = {
        'user': request.session.get('user_id'),
    }
    if request.POST.get('check') is not None:
        if int(request.POST.get('check')) == int(request.session.get('mailCode')):
            return redirect('/signin/')
    return render(request, 'whou_check.html', context)

def index_signin(request):
    if request.method == "POST":
        postsignin(request)

    context = {
        'user': request.session.get('user_id')
    }
    if request.POST.get('email') is not None:
        return render(request, "whou_main.html", context)
    return render(request, "whou_sign_in.html", context)



def index_signup(request):
    if request.method == "POST":
        postsignup(request)
    context = {
        'user': request.session.get('user_id')
    }
    if request.POST.get('email') is not None:
        context['email'] = request.POST.get('email')
        context['password'] = request.POST.get('password')
        request.session['mailCode'] = send_mail(context['email'])
        return redirect('/check/')
    return render(request, "whou_sign_up.html", context)


def index_main(request):
    context = {
        'user': request.session.get( 'user_id' )
    }

    return render(request, "whou_main.html", context)


def index_updates(request):
    context = {
        'user': request.session.get('user_id')
    }
    return render(request, "whou_updates.html", context)


