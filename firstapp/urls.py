from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('w/', views.welcome, name="welcome"),
    path('l/', views.Login_form, name="login_form"),
    #path('l/d/', views.display, name="display"),
]