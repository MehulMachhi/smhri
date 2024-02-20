# serializers.py

from rest_framework import serializers
from .models import CompanyMaster, Profile

class CompanyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMaster
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.SlugField(max_length=50, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password','password1']
    def validate(self, attrs):
        password=attrs.get('password')
        password1=attrs.pop('password1')
        if password != password1:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
