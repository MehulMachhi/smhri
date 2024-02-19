from django.contrib import admin

# Register your models here.

from .models import (
    AudiometerThresholdDecimats, BloodTest, Urine_Examination,
    Complaints, Hematology, LungFunctionTest, MicroscopicExamination,
    OtherTests, PhysiologicalTest, SystematicExamination, VisualTest, TestMaster
)

@admin.register(AudiometerThresholdDecimats)
class AudiometerThresholdDecimatsAdmin(admin.ModelAdmin):
    list_display = ('audio_employee', 'right_ac_500', 'left_ac_500', 'for_right_ear', 'for_left_ear')
    search_fields = ('audio_employee__first_name', 'audio_employee__last_name')

@admin.register(BloodTest)
class BloodTestAdmin(admin.ModelAdmin):
    list_display = ('btest_employee', 'blood_group', 'blood_cholestrol', 'creatinine', 'blood_urea')
    search_fields = ('btest_employee__first_name', 'btest_employee__last_name')

@admin.register(Urine_Examination)
class UrineExaminationAdmin(admin.ModelAdmin):
    list_display = ('urine_employee', 'volume', 'transparency', 'deposit', 'colour')
    search_fields = ('urine_employee__first_name', 'urine_employee__last_name')

@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('complaints_employee', 'present_complaints', 'occupational_complaints')
    search_fields = ('complaints_employee__first_name', 'complaints_employee__last_name')

@admin.register(Hematology)
class HematologyAdmin(admin.ModelAdmin):
    list_display = ('hlogy_employee', 'blood_group', 'hemoglobin', 'total_wbc_count', 'platelet_count')
    search_fields = ('hlogy_employee__first_name', 'hlogy_employee__last_name')

@admin.register(LungFunctionTest)
class LungFunctionTestAdmin(admin.ModelAdmin):
    list_display = ('lung_employee', 'fvc', 'fev1', 'peak_exp_flow')
    search_fields = ('lung_employee__first_name', 'lung_employee__last_name')

@admin.register(MicroscopicExamination)
class MicroscopicExaminationAdmin(admin.ModelAdmin):
    list_display = ('micro_employee', 'red_blood_cells', 'pus_cells', 'epithelial_cells', 'urine_report')
    search_fields = ('micro_employee__first_name', 'micro_employee__last_name')

@admin.register(OtherTests)
class OtherTestsAdmin(admin.ModelAdmin):
    list_display = ('othertest_employee', 'uric_acid', 'serum_cholinesterase', 'hs_crp', 'hba1c')
    search_fields = ('othertest_employee__first_name', 'othertest_employee__last_name')

@admin.register(PhysiologicalTest)
class PhysiologicalTestAdmin(admin.ModelAdmin):
    list_display = ('phy_employee', 'height', 'weight', 'blood_pressure', 'pulse')
    search_fields = ('phy_employee__first_name', 'phy_employee__last_name')

@admin.register(SystematicExamination)
class SystematicExaminationAdmin(admin.ModelAdmin):
    list_display = ('sys_employee', 'skin', 'respiratory_system', 'cardiovascular_system', 'genito_urinary_system')
    search_fields = ('sys_employee__first_name', 'sys_employee__last_name')

@admin.register(VisualTest)
class VisualTestAdmin(admin.ModelAdmin):
    list_display = ('visual_employee', 'nearvision_without_glass', 'distance_vision_without_glass')
    search_fields = ('visual_employee__first_name', 'visual_employee__last_name')

@admin.register(TestMaster)
class TestMasterAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'test_desc', 'status', 'test_model')
    search_fields = ('test_name',)
