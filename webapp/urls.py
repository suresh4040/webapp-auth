from django.urls import path, include
from .views import *

app_name='webapp'

urlpatterns = [
    path('home', index, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register_user', register_user, name='register_user'),

]
