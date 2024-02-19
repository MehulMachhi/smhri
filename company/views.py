from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import viewsets
from .models import CompanyMaster, Profile
from .serializers import CompanyMasterSerializer, ProfileSerializer

class CompanyMasterViewSet(viewsets.ModelViewSet):
    queryset = CompanyMaster.objects.all()
    serializer_class = CompanyMasterSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
