from django.urls import path

# from food_order_app.views import home, login, signup
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login', login, name='login')
    
]
