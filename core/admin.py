from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Department, Employee, Project



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):

    list_display = ['email', 'first_name', 'last_name', 'employee_id', 'department', 'role', 'salary', 'is_active']
    list_filter = ['department', 'role', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'employee_id']
    
    ordering = ['email']
    fieldsets = UserAdmin.fieldsets + (
        ('Employee Information', {
            'fields': ('employee_id', 'department', 'role', 'salary', 'phone', 'hire_date')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Employee Information', {
            'fields': ('employee_id', 'department', 'role', 'salary', 'phone')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'manager', 'status', 'start_date', 'end_date', 'is_active']
    list_filter = ['department', 'status', 'is_active', 'start_date']
    search_fields = ['name', 'description']
    filter_horizontal = ['assigned_employees']  