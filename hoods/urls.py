from django.urls import path
from .views import *

urlpatterns = [
    path('', signIn, name='signIn' ),
    path('register', register, name='register' ),
    path('signOut', signOut, name='signOut' ),
    path('home', home, name='home' ),
    path('post/<str:pk>/', post, name='post' ),
    path('profile', profile, name='profile' ),
    path('bussiness', bussiness, name='bussiness' ),
]