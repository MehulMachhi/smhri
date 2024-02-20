from rest_framework import viewsets
from .models import Appoinment, ChemicalExamination, City, Country, DiffierentialCount, Enquiry, State, UserCompany, Users, SummaryReport
from .serializers import AppoinmentSerializer, ChemicalExaminationSerializer, CitySerializer, CountrySerializer, DiffierentialCountSerializer, EnquirySerializer, StateSerializer, UserCompanySerializer, UsersSerializer, SummaryReportSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset = Appoinment.objects.all()
    serializer_class = AppoinmentSerializer
    

class ChemicalExaminationViewSet(viewsets.ModelViewSet):
    queryset = ChemicalExamination.objects.all()
    serializer_class = ChemicalExaminationSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class DiffierentialCountViewSet(viewsets.ModelViewSet):
    queryset = DiffierentialCount.objects.all()
    serializer_class = DiffierentialCountSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class UserCompanyViewSet(viewsets.ModelViewSet):
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]


class SummaryReportViewSet(viewsets.ModelViewSet):
    queryset = SummaryReport.objects.all()
    serializer_class = SummaryReportSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

