from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import EmployeeMaster
from .serializers import EmployeeMasterSerializer

class EmployeeMasterViewSet(viewsets.ModelViewSet):
    queryset = EmployeeMaster.objects.all()
    serializer_class = EmployeeMasterSerializer
