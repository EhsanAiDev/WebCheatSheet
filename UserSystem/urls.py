from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("login/" , LoginPage , name="login"),
    path("register/" , RegisterPage , name="register"),
    path("profile/<str:pk>" , ProfilePage, name="ProfilePage"),
    path("change_password/" , ChangePasswordPage , name="ChangePassword"),
    path("logout/" , LogOutPage , name="logout")
]