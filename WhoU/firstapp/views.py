from django.shortcuts import render, redirect
from .forms import UserForm
import pyrebase


def index_profile(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        return render(request, "whou_profile.html")

    return render(request, "whou_profile.html")


def index_stat(request):
    userform = UserForm()
    return render(request, "whou_statistics.html")


def index_meetings(request):
    userform = UserForm()
    return render(request, "whou_meetings.html")


def index_signin(request):
    userform = UserForm()
    return render(request, "whou_sign_in.html")


def index_signup(request):
    userform = UserForm()
    return render(request, "whou_sign_up.html")


def index_main(request):
    userform = UserForm()
    return render(request, "whou_main.html")


def index_updates(request):
    userform = UserForm()
    return render(request, "whou_updates.html")

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

def SignIn(request):
    return redirect('signin/')


def postsignin(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')
    db = firebase.database()
    db.child( "users" ).child( "Morty" )
    user = auth.sign_in_with_email_and_password(email, passw)
    data = {
        "name": "Mortimer 'Morty' Smith"
    }
    user = auth.refresh( user['refreshToken'] )
    token = auth.create_custom_token("your_custom_id")
    user = auth.sign_in_with_custom_token( token )
    if request.method == "POST":
        print(request.POST)
    return redirect('/profile/')



