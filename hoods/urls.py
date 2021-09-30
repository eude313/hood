from django.urls import path
from .views import *

urlpatterns = [
    path('', signIn, name='signIn' ),
    path('register', register, name='register' ),
    path('home', home, name='home' ),
]