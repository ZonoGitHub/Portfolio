"""
URL configuration for ProjetDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from Users.views import  register
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', register, name='register'),
    #path('accounts/', include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
   #/ path('login', login_users, name='login'),
#path('logout', logout_users, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
   
]
