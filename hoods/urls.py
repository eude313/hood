from django.urls import path
from .views import *

urlpatterns = [
    path('', signIn, name='signIn' ),
    path('register', register, name='register' ),
    path('signOut', signOut, name='signOut' ),
    path('home', home, name='home' ),
    path('profile', profile, name='profile' ),
]