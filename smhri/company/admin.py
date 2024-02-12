from django.contrib import admin
from .models import CompanyMaster

# Register your models here.

class CompanyMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'address', 'country', 'test')
    list_filter = ('name', 'phone', 'email', 'address', 'test')

    fieldsets = [
        ('Personal Info', {
            'fields': ['name', 'email', 'phone', 'pincode', 'address'],
        }),
        ('Company Info', {
            'classes': ['collapse'],
            'fields': ['company_registration_certificate', 'test'],
        })
]
        # ('Number Of', {
        #
        #     'fields': ['tube_material_of_tubes', 'tube_material_of_raws', 'tube_material_of_thermo',
        #                'tube_material_of_supports', 'tube_material_of_plugs', 'tube_material_of_coolent_tubes', ],
        # }),
        # ('Tube Specification', {
        #     'classes': ['collapse'],
        #     'fields': ['tube_spacing_or_pitch', 'inch3', 'mm3', 'total_tube_length', 'inch4', 'mm4',
        #                'top_tube_sheet_thickness', 'inch5', 'mm5', 'bottom_tube_sheet_thickness', 'inch6', 'mm6', ],
        # }),
        # ('Tube Protude', {
        #     'classes': ['collapse'],
        #     'fields': ['tube_protude_out_of_top_tube_sheet', 'inch7', 'mm7', 'tube_protude_out_of_bottom_tube_sheet',
        #                'inch8', 'mm8', 'top_dome_removable', 'top_inlet_accessible', 'top_inlet_impingment_plate',
        #                'any_projections_on_tube_sheet_describe', 'tube_sheet_material', 'dom_material', ],
        # }),
        # ('Tube Documents', {
        #     'classes': ['collapse'],
        #     'fields': ['tube_spacing_proof_document', 'reactor_tube_sheet_drawings', 'reactor_elevation_view_drawings',
        #                'other_drawings', ],
        # }),



    # def has_module_permission(self, request):
    #     return False

admin.site.register(CompanyMaster, CompanyMasterAdmin)

# from .models import Profile

# admin.site.register(Profile)