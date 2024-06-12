# myapp/views.py


from django.shortcuts import render

from .api_views.authentication import HotelRegisterView


def home(request):
    return render(request, 'index.html')

def signup(request):


    hotelname = request.POST.get('hotel_name')
    print("hotelname", hotelname)
    # a = HotelRegisterView
    # print(a.__dict__)
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
