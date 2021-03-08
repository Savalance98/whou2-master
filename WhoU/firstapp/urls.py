from django.conf.urls import url
from .views import *
from django.urls import path


urlpatterns = [
    path( 'profile/', index_profile, name='profile' ),
    path( '', index_main, name='main' ),
    path( 'meetings/', index_meetings, name='meetings' ),
    path( 'statistics/', index_stat, name='statistics' ),
    path( 'signin/', index_signin, name='signin' ),
    path( 'updates/', index_updates, name='updates' ),
    path( 'signup/', index_signup, name='signup' ),
    path ('signin/', postsignin)
]