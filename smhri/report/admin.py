from django.contrib import admin
from report.models import Appoinment
from report.models import ChemicalExamination
from report.models import City
from report.models import Country
from report.models import DiffierentialCount
from report.models import Enquiry
# from report.models import Newsletter
# from report.models import Settings
from report.models import State
# from report.models import Tokens
from report.models import UserCompany
from import_export.admin import ImportExportMixin
from report.models import Users
from .models import SummaryReport

# Register your models here.

# admin.site.register(Newsletter),

from django.contrib import admin

# Register your models here.

# class AppoinmentMasterAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('name', 'email', 'date','message'
#                     )
#     list_filter = ('name', 'email', 'date', 'message')
#     fieldsets = [
#         ('Personal info', {
#             'fields': ['name', 'email', 'date', 'message'],
#         }),
#     ]
# admin.site.register(Appoinment, AppoinmentMasterAdmin),

# class ChemicalExaminationAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ( 'volume','transparency', 'deposit', 'colour', 'sp_gravity', 'ph_reaction', 'pus_cells', 'rbc', 'epi_cells', 'casts', 'crystals', 'bacteria', 'yeast_cells',
#     'trichomonas', 'amorphous_deposit', 'albumin','sugar', 'acetone', 'bile_pigments', 'urobilinogen','bile_salts',
#                     )
#     list_filter = ('volume', 'transparency', 'deposit', 'colour', 'sp_gravity', 'ph_reaction', 'pus_cells', 'rbc', 'epi_cells', 'casts', 'crystals', 'bacteria', 'yeast_cells',
#         'trichomonas', 'amorphous_deposit', 'albumin', 'sugar', 'acetone', 'bile_pigments', 'urobilinogen', 'bile_salts')

#     fieldsets = [
#         ('ChemicalExamination Info', {
#             'fields': ['volume', 'transparency', 'deposit', 'colour', 'sp_gravity', 'ph_reaction', 'pus_cells',
#                       'rbc', 'epi_cells', 'casts', 'crystals', 'bacteria',  'yeast_cells', 'trichomonas', 'amorphous_deposit',
#                       'albumin','sugar', 'acetone', 'bile_pigments', 'bile_salts',  'urobilinogen'
#                       ],
#         }),
#         # ('About Of', {
#         #     'classes': ['collapse'],
#         #     'fields': [  ],
#         # }),
#         # ('Other', {
#         #
#         #     'fields': [  ],
#         # }),

#     ]
# admin.site.register(ChemicalExamination, ChemicalExaminationAdmin),

# class CityAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ( 'city_name', 'state',
#                     )

#     fieldsets = [
#         ('City Info', {
#             'fields': [ 'city_name', 'state'],
#         })
#     ]
# admin.site.register(City, CityAdmin),

# class CountryAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('country_name',
#                     )

#     fieldsets = [
#         ('Country Info', {
#             'fields': [ 'country_name'],
#         })
#     ]
# admin.site.register(Country, CountryAdmin),

# class DiffierentialCountAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('id','neutrophils', 'eosinophil','monocytes', 'basophil'
#                     )
#     list_filter = ('neutrophils', 'eosinophil', 'monocytes', 'basophil')

#     fieldsets = [
#         ('DiffierentialCount Info', {
#             'fields': [ 'neutrophils', 'eosinophil', 'monocytes', 'basophil'],
#         })
#     ]
# admin.site.register(DiffierentialCount, DiffierentialCountAdmin),

# class EnquiryAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone',
#                     )

#     fieldsets = [
#         ('Personal Info', {
#             'fields': ['name', 'email', 'phone', 'message'],
#         })
#     ]
# admin.site.register(Enquiry, EnquiryAdmin),

# class SettingsAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('site_title', 'timezone',
#                     )
#
#     fieldsets = [
#         ('Personal Info', {
#             'fields': ['site_title', 'timezone', 'recaptcha', 'theme'],
#         })
#     ]
# admin.site.register(Settings, SettingsAdmin),

# class StateAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ( 'state_name', 'country'
#                     )

#     fieldsets = [
#         ('Personal Info', {
#             'fields': [ 'state_name', 'country'],
#         })
#     ]
# admin.site.register(State, StateAdmin),

# class TokensAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('token', 'user', 'created'
#                     )
#
#     fieldsets = [
#         ('Personal Info', {
#             'fields': ['token', 'user', 'created'],
#         })
#     ]
# admin.site.register(Tokens, TokensAdmin),

# class UserCompanyAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ( 'user', 'company'
#                     )

#     fieldsets = [
#         ('Personal Info', {
#             'fields': [ 'user', 'company'],
#         })
#     ]
# admin.site.register(UserCompany, UserCompanyAdmin),

# class UsersAdmin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'phone'
#                     )

#     fieldsets = [
#         ('Personal Info', {
#             'fields': ['email', 'first_name', 'last_name', 'phone', 'photo', 'role', 'password',  'last_login',  'status',  'banned_users',  'user_com'],
#         }),
#         # ('About Of', {
#         #     'classes': ['collapse'],
#         #     'fields': [ ],
#         # }),
#     ]
# admin.site.register(Users, UsersAdmin)

class SummaryReportAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ( 'id','company_name','action',
                    )
    list_filter = ('company_name', )

    fieldsets = [
        ('Personal Info', {
            'fields': [ 'company_name', 'action'],
        })
    ]
admin.site.register(SummaryReport, SummaryReportAdmin),





