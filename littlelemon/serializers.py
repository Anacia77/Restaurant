from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
import bleach

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class MenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=Menu.objects.all())])

    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        if(attrs['price']<1):
            raise serializers.ValidationError('Price should not be less than 1.0')
        return super().validate(attrs)
    	
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
