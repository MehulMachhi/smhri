# admin.py

from django.contrib import admin
from .models import (
    Appoinment, ChemicalExamination, City, Country, DiffierentialCount,
    Enquiry, State, UserCompany, Users, SummaryReport
)

@admin.register(Appoinment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'message')
    search_fields = ('name', 'email', 'date')

@admin.register(ChemicalExamination)
class ChemicalExaminationAdmin(admin.ModelAdmin):
    list_display = ('volume', 'transparency', 'deposit', 'colour', 'sp_gravity')
    search_fields = ('volume', 'colour')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'state')
    search_fields = ('city_name', 'state')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
    search_fields = ('country_name',)

@admin.register(DiffierentialCount)
class DiffierentialCountAdmin(admin.ModelAdmin):
    list_display = ('neutrophils', 'eosinophil', 'monocytes', 'basophil')
    search_fields = ('neutrophils', 'eosinophil')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'country')
    search_fields = ('state_name', 'country')

@admin.register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    search_fields = ('user__email', 'company__name')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'role')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(SummaryReport)
class SummaryReportAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'action')
    search_fields = ('company_name__name', 'action')
