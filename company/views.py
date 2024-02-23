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

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,LoginSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        User.objects.create_user(**serializer.validated_data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
    
from rest_framework_simplejwt.views import TokenObtainPairView
class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Assuming you have a model named User
        user = User.objects.get(username=serializer.validated_data['username'])

        # Check if the provided password is correct
        if not user.check_password(serializer.validated_data['password']):
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

        # Assuming you are using the default User model
        token_data = {
            'username': user.username,
            'password': serializer.validated_data['password'],
        }

        # Use TokenObtainPairView to generate tokens
        token_view = TokenObtainPairView.as_view()
        token_response = token_view(request=request._request)

        # Get tokens from the response
        access_token = token_response.data['access']
        refresh_token = token_response.data['refresh']

        return Response({'access_token': access_token, 'refresh_token': refresh_token})