from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.Accounts.as_view(),name="accounts_list"),
    path('accounts/add/', views.AddAccount.as_view(),name="add_account"),
    path('accounts/edit/', views.EditAccount.as_view(),name="edit_account"),
]
