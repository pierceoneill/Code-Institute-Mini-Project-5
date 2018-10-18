from django.contrib import admin
from django.urls import path, include
from .views import index, logout, login, registration, profile
from . import urls_reset

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('password-reset/', include(urls_reset)),
]