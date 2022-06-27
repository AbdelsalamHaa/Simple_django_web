from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="homepage"),
    # This line is not for the Login, but I keep it to explain a bit about my understanding,.
    path('login/', views.login,name="login"),
    # This page is also not used but I add at the initial steps for my understanding
    path('users/', views.admin_page, name="admin_page"),

    path('profile/', views.ProfilePage.as_view(), name='profile_page'),

]
