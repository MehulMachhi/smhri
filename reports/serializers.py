from rest_framework import serializers
from .models import Appoinment, ChemicalExamination, City, Country, DiffierentialCount, Enquiry, State, UserCompany, Users, SummaryReport

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoinment
        fields = '__all__'

class ChemicalExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalExamination
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DiffierentialCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiffierentialCount
        fields = '__all__'

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class SummaryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryReport
        fields = '__all__'
