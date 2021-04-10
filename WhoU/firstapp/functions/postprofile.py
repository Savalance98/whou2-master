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


def postprofile(request, context):
    data = {
        'name': request.POST.get('name'),
        'last_name': request.POST.get('last_name'),
        'phone': request.POST.get('phone'),
        'email': request.POST.get('email'),
        'vk': request.POST.get('vk'),
    }
    context['data'] = data
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child('Users').child(context['user']).update(data)