from rest_framework import serializers
from .models import Hotel
from django.contrib.auth.hashers import make_password

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])


        return super().create(validated_data)
