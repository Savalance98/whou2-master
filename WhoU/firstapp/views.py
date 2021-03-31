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



def index_profile(request):
    try:
        userData = getUser(request)
        print(userData)
        context = {
            'user': request.session.get('user_id'),
            'data': userData
        }
        print(context)
        # print( request.session['user_id'], context['data']['Uri_image'] )
        if request.method == "POST":
            postprofile(request, context)
            return redirect('/profile/')
        return render(request, "whou_profile.html", context)
    except:
        return redirect('/')

def postprofile(request, context):
    print(1)
    data = {
        'name': request.POST.get('name'),
        'last_name': request.POST.get('last_name'),
        'phone': request.POST.get('phone'),
        'email': request.POST.get('email'),
        'vk': request.POST.get('vk'),
    }
    # print(request.FILES.get('img'))
    context['data'] = data
    # context['img'] = f(data['vk'])
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child('Users').child(context['user']).update(data)
    # print(f(data['vk']))
    # return render(request, "whou_profile.html", context)

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
        print(getUser(request))
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


