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


def index_meetings(request):
    context = {
        'user': request.session.get('user_id'),
        'lis': getUser(request, 2)
    }

    return render(request, "whou_meetings.html", context)


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
        return redirect('/signin/')
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


