from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('feed', views.newsfeed, name="feed"),
    path('signup', views.signup, name="signup"),]