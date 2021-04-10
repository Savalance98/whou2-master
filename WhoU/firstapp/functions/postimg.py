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

def postimg(file,context):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    storage.child(f"ImageDB/{context['data']['name']}").put(file, context['user'])
    url_img = storage.child(f"ImageDB/{context['data']['name']}").get_url(token=None)
    # storage.child("ImageDB/1232").put(file, context['user'])
    # url_img = storage.child("ImageDB/1232").get_url(token=None)
    data = {
        'Uri_image': url_img,
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child('Users').child(context['user']).update(data)