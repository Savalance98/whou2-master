from django.shortcuts import render, redirect
from .forms import UserForm
import pyrebase
from requests.exceptions import HTTPError
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
global Info
global Id


def index_profile(request):
    print(cookies_demo(request))
    return render(request, "whou_profile.html")


def index_stat(request):
    userform = UserForm()
    return render(request, "whou_statistics.html")


def index_meetings(request):
    userform = UserForm()
    return render(request, "whou_meetings.html")


def index_signin(request):
    userform = UserForm()
    if request.method == "POST":
        postsignin(request)
    context = {}
    print(context)
    if request.POST.get('email') is not None:
        context['email'] = request.POST.get('email')
        request.session.set_test_cookie()
        # if request.session.test_cookie_worked():
        #     SESSION_COOKIE_NAME = 'test'
        #     print(request.session)
        # request.session.set_test_cookie()
        # request.session['email'] = request.POST.get('email')
        # if request.method == 'POST':
        #     if request.session.test_cookie_worked():
        #         request.session.delete_test_cookie()
        #         return HttpResponse("You're logged in.")
        #     else:
        #         return HttpResponse("Please enable cookies and try again.")
    return render(request, "whou_sign_in.html", context)


def index_signup(request):
    if request.method == "POST":
        postsignup(request)
    context = {}
    if request.POST.get('email') is not None:
        context['email'] = request.POST.get('email')
    return render(request, "whou_sign_up.html", context)


def index_main(request):
    # from pprint import pprint
    # request.session['user_data'] = {}
    # pprint(dict(request.session))
    userform = UserForm()
    return render(request, "whou_main.html")


def index_updates(request):
    userform = UserForm()
    return render(request, "whou_updates.html")

# def SignIn(request):
#     return redirect('signin/')


def postsignin(request):
    Info = None
    Id = None
    # print(request)
    email = request.POST.get('email')
    print(email)
    passw = request.POST.get('password')
    print(passw)
    config = {
        'apiKey': "AIzaSyBSxWNN_VKfsSTwCp3yjoe3x_W0RjNivdw",
        'authDomain': "whou-d361d.firebaseapp.com",
        'databaseURL': "https://whou-d361d.firebaseio.com",
        'projectId': "whou-d361d",
        'storageBucket': "whou-d361d.appspot.com",
        'messagingSenderId': "994830820246",
        'appId': "1:994830820246:web:94eecba0e57f35704673b7",
        'measurementId': "G-SY3JH2ZEKQ"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
        auth.send_email_verification(user['idToken'])
        # auth.send_password_reset_email(email)
        # print(auth.get_account_info(user['idToken']))

        Info = auth.get_account_info(user['idToken'])['users']
        Id  = Info[0]['localId']
        print(Id)
        print(Info)

        # print(user, type(user))
        # print(db.child('Users').get('name'))
    except HTTPError as error:
        print(error)
    print("Работает")

def postsignup(request):
    config = {
        'apiKey': "AIzaSyBSxWNN_VKfsSTwCp3yjoe3x_W0RjNivdw",
        'authDomain': "whou-d361d.firebaseapp.com",
        'databaseURL': "https://whou-d361d.firebaseio.com",
        'projectId': "whou-d361d",
        'storageBucket': "whou-d361d.appspot.com",
        'messagingSenderId': "994830820246",
        'appId': "1:994830820246:web:94eecba0e57f35704673b7",
        'measurementId': "G-SY3JH2ZEKQ"
    }


    data = {
        'email': request.POST.get('email'),
        'pass': request.POST.get('password'),
        'name': request.POST.get('name'),
        'phone': request.POST.get('phone'),
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child('Users').child('qwerty').set(data)
    print('Работаеттттттттт')


def cookies_demo(request):
    response = render(request, 'whou_sign_in.html')
    response.set_cookie('demo-cookies', '123456789')
    print(1)
    return response





