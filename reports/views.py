from rest_framework import viewsets
from .models import Appoinment, ChemicalExamination, City, Country, DiffierentialCount, Enquiry, State, UserCompany, Users, SummaryReport
from .serializers import AppoinmentSerializer, ChemicalExaminationSerializer, CitySerializer, CountrySerializer, DiffierentialCountSerializer, EnquirySerializer, StateSerializer, UserCompanySerializer, UsersSerializer, SummaryReportSerializer

class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset = Appoinment.objects.all()
    serializer_class = AppoinmentSerializer

class ChemicalExaminationViewSet(viewsets.ModelViewSet):
    queryset = ChemicalExamination.objects.all()
    serializer_class = ChemicalExaminationSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DiffierentialCountViewSet(viewsets.ModelViewSet):
    queryset = DiffierentialCount.objects.all()
    serializer_class = DiffierentialCountSerializer

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class UserCompanyViewSet(viewsets.ModelViewSet):
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class SummaryReportViewSet(viewsets.ModelViewSet):
    queryset = SummaryReport.objects.all()
    serializer_class = SummaryReportSerializer
