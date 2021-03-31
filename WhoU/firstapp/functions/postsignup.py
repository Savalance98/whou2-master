import pyrebase
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

def postsignup(request):
    data = {
        'email': request.POST.get('email'),
        'pass': request.POST.get('password'),
        'name': request.POST.get('name'),
        'phone': request.POST.get('phone'),
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    auth = firebase.auth()
    localId = auth.create_user_with_email_and_password(data['email'], data['pass'])['localId']
    db.child('Users').child(localId).set(data)
    print(localId, data)
    print('Работаеттттттттт')