"""Definiuje wzorce adresów URL dla aplikacji Users"""

from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from . import views

urlpatterns = [
    #strona logowania
    url(r'^users/login/$', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^users/register/$', views.register, name='register'),
]
