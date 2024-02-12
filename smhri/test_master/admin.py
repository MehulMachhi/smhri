from django.contrib import admin
from test_master.models import AudiometerThresholdDecimats
from test_master.models import BloodTest
from test_master.models import Complaints
from test_master.models import Hematology
from test_master.models import LungFunctionTest
from test_master.models import MicroscopicExamination
from test_master.models import VisualTest
from test_master.models import OtherTests
from test_master.models import PhysiologicalTest
from test_master.models import SystematicExamination
from test_master.models import TestMaster
from test_master.models import Urine_Examination
from import_export.admin import ExportActionMixin

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin
# from .forms import CustomConfirmImportForm, CustomImportForm
# Register your models here.




class AudiometerThresholdDecimatsAdmin(admin.ModelAdmin):
    list_display = ('audio_employee','right_ac_500', 'right_bc_500', 'right_ac_1000', 'right_bc_1000','right_ac_2000',
                       'right_bc_2000', 'right_ac_4000', 'right_bc_4000', 'right_ac_5000', 'right_bc_5000','left_ac_500',
                       'left_bc_500','left_ac_1000','left_bc_1000','left_ac_2000', 'left_bc_2000','left_ac_4000','left_bc_4000',
                       'left_ac_5000','left_bc_5000', 'for_right_ear',  'for_left_ear', 'audiometery','xray_report', 'ultra_sonographic')
                       
    list_filter = ('audio_employee','right_ac_500', 'right_bc_500', 'right_ac_1000', 'right_bc_1000','right_ac_2000',
                       'right_bc_2000', 'right_ac_4000', 'right_bc_4000', 'right_ac_5000', 'right_bc_5000','left_ac_500',
                       'left_bc_500','left_ac_1000','left_bc_1000','left_ac_2000', 'left_bc_2000','left_ac_4000','left_bc_4000',
                       'left_ac_5000','left_bc_5000', 'for_right_ear',  'for_left_ear', 'audiometery','xray_report', 'ultra_sonographic')
                       

    fieldsets = [
        ('AudiometerThresholdDecimatsAdmin', {
            'fields': ['audio_employee','right_ac_500', 'right_bc_500', 'right_ac_1000', 'right_bc_1000','right_ac_2000',
                       'right_bc_2000', 'right_ac_4000', 'right_bc_4000', 'right_ac_5000', 'right_bc_5000','left_ac_500',
                       'left_bc_500','left_ac_1000','left_bc_1000','left_ac_2000', 'left_bc_2000','left_ac_4000','left_bc_4000',
                       'left_ac_5000','left_bc_5000', 'for_right_ear',  'for_left_ear', 'audiometery','xray_report', 'ultra_sonographic'
                       ]})
        # }),
        # ('AudiometerThresholdDecimatsAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [
        #                  ],
        # }),
        # ('AudiometerThresholdDecimatsAdmin3', {
        #     'classes': ['collapse'],
        #     'fields': [ ],
        # }),
    ]
admin.site.register(AudiometerThresholdDecimats, AudiometerThresholdDecimatsAdmin)

class BloodTestAdmin(admin.ModelAdmin):
    list_display = ('btest_employee','blood_group', 'blood_cholestrol', 'creatinine', 'blood_urea', 'fasting_blood_glucose','random_blood_glucose',
                       'post_prandial_blood_glucose', 'total_bilirubin', 'direct_bilirubin', 'indirect_bilirubin', 'sgpt',  'sgot',
                       'alkaline_phosphatase', 'ggt',  'total_cholesterol', 'triglycerides',  'direct_hdl', 'vldl', 'ldl',  'ch_ratio',
                       'lh_ratio', 'rdw_sd',  'plcc', 'plcr', 'vitaminb12',  'vitamind3',  'hcv', 'psa', 'bun')
    
    list_filter = ('btest_employee', 'blood_group','blood_cholestrol', 'creatinine', 'blood_urea', 'fasting_blood_glucose','random_blood_glucose',
                       'post_prandial_blood_glucose', 'total_bilirubin', 'direct_bilirubin', 'indirect_bilirubin', 'sgpt',  'sgot',
                       'alkaline_phosphatase', 'ggt',  'total_cholesterol', 'triglycerides',  'direct_hdl', 'vldl', 'ldl',  'ch_ratio',
                       'lh_ratio', 'rdw_sd',  'plcc', 'plcr', 'vitaminb12',  'vitamind3',  'hcv', 'psa', 'bun')

    fieldsets = [
        ('BloodTestAdmin', {
            'fields': ['btest_employee', 'blood_group','blood_cholestrol', 'creatinine', 'blood_urea', 'fasting_blood_glucose','random_blood_glucose',
                       'post_prandial_blood_glucose', 'total_bilirubin', 'direct_bilirubin', 'indirect_bilirubin', 'sgpt',  'sgot',
                       'alkaline_phosphatase', 'ggt',  'total_cholesterol', 'triglycerides',  'direct_hdl', 'vldl', 'ldl',  'ch_ratio',
                       'lh_ratio', 'rdw_sd',  'plcc', 'plcr', 'vitaminb12',  'vitamind3',  'hcv', 'psa', 'bun'
                       ],
        }),
        # ('BloodTestAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [
        #                 ],
        # }),
        # ('BloodTestAdmin3', {
        #     'classes': ['collapse'],
        #     'fields': [  ],

    ]
admin.site.register(BloodTest, BloodTestAdmin)

class Urine_ExaminationAdmin(admin.ModelAdmin):
    list_display = ('urine_employee', 'volume', 'transparency', 'deposit', 'colour','sp_gravity',
                       'ph_reaction', 'pus_cells', 'rbc', 'epi_cells', 'casts',  'crystals',
                       'bacteria', 'yeast_cells',  'trichomonas', 'amorphous_deposit',  'albumin', 'sugar', 'acetone',  'bile_pigments',
                       'bile_salts', 'urobilinogen'
                    )
                    
    list_filter = ('urine_employee', 'volume', 'transparency', 'deposit', 'colour','sp_gravity',
                       'ph_reaction', 'pus_cells', 'rbc', 'epi_cells', 'casts',  'crystals',
                       'bacteria', 'yeast_cells',  'trichomonas', 'amorphous_deposit',  'albumin', 'sugar', 'acetone',  'bile_pigments',
                       'bile_salts', 'urobilinogen'
                    )

    fieldsets = [
        ('Urine_ExaminationAdmin', {
            'fields': ['urine_employee', 'volume', 'transparency', 'deposit', 'colour','sp_gravity',
                       'ph_reaction', 'pus_cells', 'rbc', 'epi_cells', 'casts',  'crystals',
                       'bacteria', 'yeast_cells',  'trichomonas', 'amorphous_deposit',  'albumin', 'sugar', 'acetone',  'bile_pigments',
                       'bile_salts', 'urobilinogen', 'red_blood_cells', 'epithelial_cells', 'urine_report', 'crystais', 'material'
                       ],
        }),
        # ('BloodTestAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [
        #                 ],
        # }),
        # ('BloodTestAdmin3', {
        #     'classes': ['collapse'],
        #     'fields': [  ],

    ]
admin.site.register(Urine_Examination, Urine_ExaminationAdmin)

class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('complaints_employee', 'present_complaints', 'occupational_complaints','personal_health_history',
                       'past_history', 'allergic_to', 'id_mark_scar',  'id_mark_mole'
                    )
                    
    list_filter = ('complaints_employee', 'present_complaints', 'occupational_complaints', 'family_health_history', 'personal_health_history',
                       'past_history', 'allergic_to', 'id_mark_scar',  'id_mark_mole'
                    )

    fieldsets = [
        ('ComplaintsAdmin', {
            'fields': ['complaints_employee', 'present_complaints', 'occupational_complaints', 'family_health_history', 'personal_health_history',
                       'past_history', 'allergic_to', 'id_mark_scar',  'id_mark_mole'],
        }),
        # ('ComplaintsAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [  ],
        # }),
    ]
admin.site.register(Complaints, ComplaintsAdmin)

class HematologyAdmin(admin.ModelAdmin):
    list_display = ('hlogy_employee', 'blood_group', 'hemoglobin', 'total_wbc_count', 'polymorphs', 'lymphocytes', 'eosinophils',
                       'monocytes', 'basophils', 'leucocytes_count', 'platelet_count', 'esr', 'hct', 'rdw_cv', 'pdw',
                       'mpv', 'mch', 'mchc', 'pct', 'mcv', 'peripheral_smear'
                    )
                    
    list_filter = ('hlogy_employee', 'blood_group', 'hemoglobin', 'total_wbc_count', 'polymorphs', 'lymphocytes', 'eosinophils',
                       'monocytes', 'basophils', 'leucocytes_count', 'platelet_count', 'esr', 'hct', 'rdw_cv', 'pdw',
                       'mpv', 'mch', 'mchc', 'pct', 'mcv', 'peripheral_smear'
                    )

    fieldsets = [
        ('HematologyAdmin', {
            'fields': [ 'hlogy_employee', 'blood_group', 'hemoglobin', 'total_wbc_count', 'polymorphs', 'lymphocytes', 'eosinophils',
                       'monocytes', 'basophils', 'leucocytes_count', 'platelet_count', 'esr', 'hct', 'rdw_cv', 'pdw',
                       'mpv', 'mch', 'mchc', 'pct', 'mcv', 'peripheral_smear'],
        }),
        # ('HematologyAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [ ],
        # }),
        # ('HematologyAdmin3', {
        #     'classes': ['collapse'],
        #     'fields': [ ],
        # }),
    ]
admin.site.register(Hematology, HematologyAdmin)

class LungFunctionTestAdmin(admin.ModelAdmin):
    list_display = ('lung_employee','fvc', 'fev1', 'fev1_fvc', 'peak_exp_flow', 'fef50', 'fvc_predicted', 'fev1_predicted', 'fev1_fvc_predicted',
                       'pefr_predicted',  'fef50_predicted',  'fvc_per_predicted', 'fev1_per_predicted', 'fev1_fvc_per_predicted',  'pefr_per_predicted',
                       'fef50_per_predicted',  'spirometry'
                    )
                    
    list_filter =  ('lung_employee','fvc', 'fev1', 'fev1_fvc', 'peak_exp_flow', 'fef50', 'fvc_predicted', 'fev1_predicted', 'fev1_fvc_predicted',
                       'pefr_predicted',  'fef50_predicted',  'fvc_per_predicted', 'fev1_per_predicted', 'fev1_fvc_per_predicted',  'pefr_per_predicted',
                       'fef50_per_predicted',  'spirometry'
                    )

    fieldsets = [
        ('LungFunctionTestAdmin', {
            'fields': ['lung_employee','fvc', 'fev1', 'fev1_fvc', 'peak_exp_flow', 'fef50', 'fvc_predicted', 'fev1_predicted', 'fev1_fvc_predicted',
                       'pefr_predicted',  'fef50_predicted',  'fvc_per_predicted', 'fev1_per_predicted', 'fev1_fvc_per_predicted',  'pefr_per_predicted',
                       'fef50_per_predicted',  'spirometry' ],
        }),
        # ('LungFunctionTestAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [  ],
        # }),
        # ('LungFunctionTestAdmin3', {
        #     'classes': ['collapse'],
        #     'fields': [  ],
        # }),
    ]
admin.site.register(LungFunctionTest, LungFunctionTestAdmin)

class MicroscopicExaminationAdmin(admin.ModelAdmin):
    list_display = ('micro_employee', 'red_blood_cells', 'pus_cells', 'epithelial_cells', 'urine_report', 'casts', 'crystais', 'material'
                    )
                    
    list_filter = ('micro_employee', 'red_blood_cells', 'pus_cells', 'epithelial_cells', 'urine_report', 'casts', 'crystais', 'material'
                    )

    fieldsets = [
        ('MicroscopicExaminationAdmin', {
            'fields': ['micro_employee', 'red_blood_cells', 'pus_cells', 'epithelial_cells', 'urine_report', 'casts', 'crystais', 'material'],
        }),
        # ('MicroscopicExaminationAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [ ],
        # }),

    ]
admin.site.register(MicroscopicExamination, MicroscopicExaminationAdmin)


class OtherTestsAdmin(admin.ModelAdmin):
    list_display = ('othertest_employee','uric_acid', 'serum_cholinesterase', 'hs_crp', 'gppd', 'hba1c', 'avg_blood_glucose_level', 'hbsag',
                       'hiv_result', 'hiv_method','hiv_remark', 's_protein_total', 's_albumin_bcg',  's_globulin', 'ag_ratio', 'acid_fast_bacilli',
                        'stool_color', 'stool_blood', 'stool_mucus', 'stool_adults_warm', 'stool_parasites', 'stool_pus', 'stool_ph', 'stool_occult_blood',
                        'stool_reducing_substances','stool_rbcs', 'stool_puscells',  'stool_fat_globules', 'stool_macrophages','stool_epithelial_cell',
                        'stool_muscle_fibers',  'stool_vegetable_cell',  'stool_bacteria', 'stool_cyst', 'stool_ova',  'stool_trophozoites',  'stool_larva',
                        'stool_yeast_cells', 'stool_starch_granules',  'thyroid_tsh',  'thyroid_t3',  'thyroid_t4',   'vdrl',
                    )
                    
    list_filter = ('othertest_employee','uric_acid', 'serum_cholinesterase', 'hs_crp', 'gppd', 'hba1c', 'avg_blood_glucose_level', 'hbsag',
                       'hiv_result', 'hiv_method','hiv_remark', 's_protein_total', 's_albumin_bcg',  's_globulin', 'ag_ratio', 'acid_fast_bacilli',
                        'stool_color', 'stool_blood', 'stool_mucus', 'stool_adults_warm', 'stool_parasites', 'stool_pus', 'stool_ph', 'stool_occult_blood',
                        'stool_reducing_substances','stool_rbcs', 'stool_puscells',  'stool_fat_globules', 'stool_macrophages','stool_epithelial_cell',
                        'stool_muscle_fibers',  'stool_vegetable_cell',  'stool_bacteria', 'stool_cyst', 'stool_ova',  'stool_trophozoites',  'stool_larva',
                        'stool_yeast_cells', 'stool_starch_granules',  'thyroid_tsh',  'thyroid_t3',  'thyroid_t4',   'vdrl',
                    )

    fieldsets = [
        ('OtherTestsAdmin', {
            'fields': ['othertest_employee','uric_acid', 'serum_cholinesterase', 'hs_crp', 'gppd', 'hba1c', 'avg_blood_glucose_level', 'hbsag',
                       'hiv_result', 'hiv_method','hiv_remark', 's_protein_total', 's_albumin_bcg',  's_globulin', 'ag_ratio', 'acid_fast_bacilli',
                        'stool_color', 'stool_blood', 'stool_mucus', 'stool_adults_warm', 'stool_parasites', 'stool_pus', 'stool_ph', 'stool_occult_blood',
                        'stool_reducing_substances','stool_rbcs', 'stool_puscells',  'stool_fat_globules', 'stool_macrophages','stool_epithelial_cell',
                        'stool_muscle_fibers',  'stool_vegetable_cell',  'stool_bacteria', 'stool_cyst', 'stool_ova',  'stool_trophozoites',  'stool_larva',
                        'stool_yeast_cells', 'stool_starch_granules',  'thyroid_tsh',  'thyroid_t3',  'thyroid_t4',   'vdrl',
                        ],
        }),
        # ('OtherTestsAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [
        #                ,    ],
        # }),
        # ('OtherTestsAdmin3', {
        #     'classes': ['collapse'],
        #     'fields': [
        #         ,   ],
        # }),
        # ('OtherTestsAdmin4', {
        #     'classes': ['collapse'],
        #     'fields': [
        #
        #              ],
        # }),

    ]
admin.site.register(OtherTests, OtherTestsAdmin)

class PhysiologicalTestAdmin(admin.ModelAdmin):
    list_display = ('phy_employee', 'height', 'weight', 'blood_pressure', 'pulse', 'heart_sound', 'chest_on_expiration', 'chest_on_inspiration',
                       'waist',  'hips', 'waist_hip_ratio', 'remarks_and_advice'
                    )
                    
    list_filter = ('phy_employee', 'height', 'weight', 'blood_pressure', 'pulse', 'heart_sound', 'chest_on_expiration', 'chest_on_inspiration',
                       'waist',  'hips', 'waist_hip_ratio', 'remarks_and_advice'
                    )

    fieldsets = [
        ('PhysiologicalTestAdmin', {
            'fields': ['phy_employee', 'height', 'weight', 'blood_pressure', 'pulse', 'heart_sound', 'chest_on_expiration', 'chest_on_inspiration',
                       'waist',  'hips', 'waist_hip_ratio', 'remarks_and_advice'
                       ],
        }),
        # ('PhysiologicalTestAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [  ],
        # }),

    ]
admin.site.register(PhysiologicalTest, PhysiologicalTestAdmin)

class SystematicExaminationAdmin(admin.ModelAdmin):
    list_display = ('sys_employee', 'skin', 'respiratory_system', 'cardiovascular_system', 'genito_urinary_system', 'skeletal_system',
                       'cns',  'breath_sound', 'abdomen',  'other_finding',   'ecg_report'
                    )
                    
    list_filter = ('sys_employee', 'skin', 'respiratory_system', 'cardiovascular_system', 'genito_urinary_system', 'skeletal_system',
                       'cns',  'breath_sound', 'abdomen',  'other_finding',   'ecg_report'
                    )

    fieldsets = [
        ('SystematicExaminationAdmin', {
            'fields': [ 'sys_employee', 'skin', 'respiratory_system', 'cardiovascular_system', 'genito_urinary_system', 'skeletal_system',
                       'cns',  'breath_sound', 'abdomen',  'other_finding',   'ecg_report'],
        }),
        # ('SystematicExaminationAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),

    ]
admin.site.register(SystematicExamination, SystematicExaminationAdmin)

class VisualTestAdmin(admin.ModelAdmin):
    list_display = ('visual_employee', 'nearvision_without_glass', 'distance_vision_without_glass', 'nearvision_with_glass', 'distance_vision_with_glass',
                       'nearvision_without_glass_right', 'distance_vision_without_glass_right', 'nearvision_with_glass_right', 'distance_vision_with_glass_right',
                       'vision_remark' 
                    )
                    
    list_filter = ('visual_employee', 'nearvision_without_glass', 'distance_vision_without_glass', 'nearvision_with_glass', 'distance_vision_with_glass',
                       'nearvision_without_glass_right', 'distance_vision_without_glass_right', 'nearvision_with_glass_right', 'distance_vision_with_glass_right',
                       'vision_remark' 
                    )

    fieldsets = [
        ('VisualTestAdmin', {
            'fields': ['visual_employee', 'nearvision_without_glass', 'distance_vision_without_glass', 'nearvision_with_glass', 'distance_vision_with_glass',
                       'nearvision_without_glass_right', 'distance_vision_without_glass_right', 'nearvision_with_glass_right', 'distance_vision_with_glass_right',
                       'vision_remark' ],
        }),
        # ('VisualTestAdmin2', {
        #     'classes': ['collapse'],
        #     'fields': [  ],
        # }),

    ]
admin.site.register(VisualTest, VisualTestAdmin)

class TestMasterAdmin( admin.ModelAdmin):
    list_display = ('test_name', 'test_desc', 'status', 'test_model'
                    )
                    
    list_filter = ('test_name', 'test_desc', 'status', 'test_model'
                    )

    fieldsets = [
        ('TestMasterAdmin', {
            'fields': ['test_name', 'test_desc', 'status', 'test_model'],
        }),

    ]
admin.site.register(TestMaster, TestMasterAdmin)










