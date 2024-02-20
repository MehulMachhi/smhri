from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import viewsets
from .models import CompanyMaster, Profile
from .serializers import CompanyMasterSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CompanyMasterViewSet(viewsets.ModelViewSet):
    queryset = CompanyMaster.objects.all()
    serializer_class = CompanyMasterSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated] 

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated] 
