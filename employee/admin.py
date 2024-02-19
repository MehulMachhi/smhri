

from django.contrib import admin
from .models import EmployeeMaster

@admin.register(EmployeeMaster)
class EmployeeMasterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_no', 'ticket_no', 'designation', 'status')
    search_fields = ('first_name', 'last_name', 'employee_no', 'ticket_no')
    list_filter = ('status', 'designation', 'test_type')
