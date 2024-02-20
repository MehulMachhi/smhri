"""
URL configuration for smrhi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from reports.views import AppoinmentViewSet, ChemicalExaminationViewSet, CityViewSet, CountryViewSet, DiffierentialCountViewSet, EnquiryViewSet, StateViewSet, UserCompanyViewSet, UsersViewSet, SummaryReportViewSet
from textmaster.views import (
    AudiometerThresholdDecimatsViewSet, BloodTestViewSet,
    Urine_ExaminationViewSet, ComplaintsViewSet,
    HematologyViewSet, LungFunctionTestViewSet,
    MicroscopicExaminationViewSet, OtherTestsViewSet,
    PhysiologicalTestViewSet, SystematicExaminationViewSet,
    VisualTestViewSet
)
from employee.views import EmployeeMasterViewSet
from company.views import CompanyMasterViewSet, ProfileViewSet,RegisterViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#RegisterViewSet
router = DefaultRouter()
router.register('reports/appoinment', AppoinmentViewSet)
router.register('reports/chemical_examination', ChemicalExaminationViewSet)
router.register('reports/city', CityViewSet)
router.register('reports/country', CountryViewSet)
router.register('reports/differential_count', DiffierentialCountViewSet)
router.register('reports/enquiry', EnquiryViewSet)
router.register('reports/state', StateViewSet)
router.register('reports/user_company', UserCompanyViewSet)
router.register('reports/users', UsersViewSet)
router.register('reports/summary_report', SummaryReportViewSet)
router.register('audiometer_threshold_decimats', AudiometerThresholdDecimatsViewSet, basename='audiometer_threshold_decimats')
router.register('blood_test', BloodTestViewSet, basename='blood_test')
router.register('urine_examination', Urine_ExaminationViewSet, basename='urine_examination')
router.register('complaints', ComplaintsViewSet, basename='complaints')
router.register('hematology', HematologyViewSet, basename='hematology')
router.register('lung_function_test', LungFunctionTestViewSet, basename='lung_function_test')
router.register('microscopic_examination', MicroscopicExaminationViewSet, basename='microscopic_examination')
router.register('other_tests', OtherTestsViewSet, basename='other_tests')
router.register('physiological_test', PhysiologicalTestViewSet, basename='physiological_test')
router.register('systematic_examination', SystematicExaminationViewSet, basename='systematic_examination')
router.register('visual_test', VisualTestViewSet, basename='visual_test')
router.register('employee_master', EmployeeMasterViewSet)
router.register('company_master', CompanyMasterViewSet)
router.register('profile', ProfileViewSet)
router.register('register', RegisterViewSet, basename='register')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
