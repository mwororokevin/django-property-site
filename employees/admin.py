from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_name',
        'position',
        'phone_number',
        'email'
    )

admin.site.register(Employee, EmployeeAdmin)