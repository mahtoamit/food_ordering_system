from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('admindashboard/', admin_dashboard, name='admin_dashboard'),
    
]

