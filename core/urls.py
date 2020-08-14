from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('test/', test, name="test"),
    path('sellers/', sellers, name="sellers"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('registration/', registration, name="registration"),
    path('personaloffice/<int:pk>', personaloffice, name="personaloffice"),
    path('change-password/', change_password, name="change-password")
]