import pyrebase
from django.http import HttpResponse

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

def postsignin(request):
    email = request.POST.get('email')
    passw = request.POST.get('password')

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
        # auth.send_email_verification(user['idToken'])
        Info = auth.get_account_info(user['idToken'])['users']
        # print('\n\n\n\n')
        # print(Info)
        # print( '\n\n\n\n' )
        request.session['user_id'] = Info[0]['localId']
        # auth.send_password_reset_email(email)
        #         # print(auth.get_account_info(user['idToken']))

    except HTTPError as error:
        print(error)
    # print("Работает")