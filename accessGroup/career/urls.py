from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="homepage"),
    # path('login/', views.login,name="login"),
    path('users/', views.admin_page, name="admin_page"),
    path('profile/', views.ProfilePage.as_view(), name='profile_page'),

]
