from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Hotel

class EmailBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
     
        try:
            hotel = Hotel.objects.get(email=email)
        except Hotel.DoesNotExist:
            return None

        if hotel and check_password(password, hotel.password):
            return hotel
        return None

    def get_user(self, hotel_id):
        try:
            return Hotel.objects.get(pk=hotel_id)
        except Hotel.DoesNotExist:
            return None
        

