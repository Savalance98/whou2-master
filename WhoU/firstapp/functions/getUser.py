import pyrebase
from .getUserHist import *


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

def getUser(request, h = 0 ): # Получить данные пользователя по его uid
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    data = {}
    lis = []
    try:
        for e in db.child('Users').child(request.session.get('user_id')).get().each():
            data[e.key()] = e.val()
        if data['Uri_image'] == 'nulls' or data['Uri_image'] == 'null':
            data['Uri_image'] = f(data['vk']) if f(data['vk']) else "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Man_silhouette.svg/1920px-Man_silhouette.svg.png"
        if h != 0:
            hist = list(data['history2'].split('|'))
            hist.pop(0)
            # print(vk.users.get(user_ids=hist[0], fields='photo_max'))
            for r in hist:
                data2 = {}
                for e in db.child('Users').child(r).get().each():
                    data2[e.key()] = e.val()
                if data2['Uri_image'] == 'nulls' or data2['Uri_image'] == 'null':
                    data2['Uri_image'] = f(data2['vk']) if f(data2['vk']) else "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Man_silhouette.svg/1920px-Man_silhouette.svg.png"
                lis.append(data2)
            return lis
        return data
    except:
        return request.session.get('user_id')