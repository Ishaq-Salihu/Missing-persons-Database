from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','password','username')