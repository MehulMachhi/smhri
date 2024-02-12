from django.contrib import admin

# Register your models here.

from employee.models import EmployeeMaster

class EmployeeMasterAdmin(admin.ModelAdmin):
    list_display = ( 'id','first_name', 'middle_name','last_name','sex','company','ticket_no', 'pan_number','date_joining', 'designation','department','address',
    'city','birthdate','fitness_certificate_date','previous_certificate_number','collection_date','test_date','status','name_pref', 'test_type', 'employee_no', 'aadhar_card_no',
                    )
                    
    list_filter = (
        'first_name','sex', 'company', 'ticket_no',  'date_joining',
        'designation', 'department','city', 'birthdate', 'fitness_certificate_date',
        'collection_date', 'test_date', 'status', 'name_pref', 'test_type', 'employee_no',
      
    )

    list_display_links = ['first_name']
    fieldsets = [
        ('Profile', {
            'fields': [ 'name_pref','test_type', 'first_name', 'middle_name', 'last_name', 'sex',
                        ],
        }),
        ('Company', {
            'classes': ['collapse'],
            'fields': ['list_company', 'company', 'employee_no', 'ticket_no', 'aadhar_card_no', 'pan_number'],
        }),
        ('Details', {

            'fields': ['date_joining',  'designation', 'department'],
        }),
        ('Contact', {
            'classes': ['collapse'],
            'fields': [ 'address', 'city', ],
        }),
        ('Info', {
            'classes': ['collapse'],
            'fields': ['birthdate', 'photo', 'fitness_certificate_date',  'previous_certificate_number'],
        }),
        ('Add Test', {
            'classes': ['collapse'],
            'fields': ['collection_date', 'test_date', 'status', 'show',  'AudiometerThresholdDecimats', 'BloodTest',
                       'Complaints', 'Hematology' ,'LungFunctionTest', 'MicroscopicExamination', 'OtherTests', 'PhysiologicalTest',
                       'SystematicExamination', 'VisualTest'],
        }),

        # ('BloodTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('Complaints', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('Hematology', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('LungFunctionTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('MicroscopicExamination', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('OtherTests', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('PhysiologicalTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('SystematicExamination', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('VisualTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # # ('TestMaster', {
        # #     'classes': ['collapse'],
        # #     'fields': [],
        # # }),

    ]

    # def has_module_permission(self, request):
    #     return False



admin.site.register(EmployeeMaster, EmployeeMasterAdmin)