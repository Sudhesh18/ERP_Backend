from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.db.models import Count, Sum
from .models import Department, Employee, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer
from django.http import HttpResponse
import csv
from datetime import datetime


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']

class IsEmployeeReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in ['GET']:  
            return True
        return request.user.role in ['admin', 'manager'] 


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  
        return [IsAuthenticated(), IsManagerOrAdmin()]  


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  
        return [IsAuthenticated(), IsAdmin()] 


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  
        return [IsAuthenticated(), IsManagerOrAdmin()]  


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employees_by_department(request):
    departments = Department.objects.all()
    result = []
    for dept in departments:
        result.append({
            'department': dept.name,
            'employee_count': dept.employees.count()
        })
    return Response(result)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def salary_cost_per_department(request):
    departments = Department.objects.all()
    result = []
    for dept in departments:
        total_salary = 0
        for employee in dept.employees.all():
            total_salary += employee.salary
        result.append({
            'department': dept.name,
            'total_salary': total_salary,
            'employee_count': dept.employees.count()
        })
    return Response(result)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_projects_list(request):
    active_projects = Project.objects.filter(is_active=True)
    result = []
    for project in active_projects:
        result.append({
            'name': project.name,
            'department': project.department.name,
            'status': project.status,
            'start_date': project.start_date
        })
    return Response(result)
  
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsManagerOrAdmin])
def export_employees_csv(request):
    """Export all employees to CSV"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="employees_{datetime.now().date()}.csv"'
    
    writer = csv.writer(response)
    
 
    writer.writerow([
        'Employee ID', 'First Name', 'Last Name', 'Email', 
        'Department', 'Role', 'Salary', 'Hire Date', 'Phone'
    ])
    
 
    employees = Employee.objects.all().select_related('department')
    for employee in employees:
        writer.writerow([
            employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.email,
            employee.department.name if employee.department else 'None',
            employee.role,
            employee.salary,
            employee.hire_date,
            employee.phone or 'N/A'
        ])
    
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsManagerOrAdmin])
def export_departments_csv(request):
    """Export all departments to CSV"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="departments_{datetime.now().date()}.csv"'
    
    writer = csv.writer(response)
    
    writer.writerow([
        'Department ID', 'Name', 'Description', 'Employee Count', 
        'Total Salary Cost', 'Created Date'
    ])
    

    departments = Department.objects.annotate(
        emp_count=Count('employees'),
        total_salary=Sum('employees__salary')
    )
    
    for dept in departments:
        writer.writerow([
            dept.id,
            dept.name,
            dept.description,
            dept.emp_count,
            dept.total_salary or 0,
            dept.created_at.date()
        ])
    
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsManagerOrAdmin])
def export_projects_csv(request):
    """Export all projects to CSV"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="projects_{datetime.now().date()}.csv"'
    
    writer = csv.writer(response)
    

    writer.writerow([
        'Project ID', 'Name', 'Description', 'Department', 
        'Manager', 'Status', 'Start Date', 'End Date', 'Active'
    ])
    

    projects = Project.objects.select_related('department', 'manager')
    for project in projects:
        writer.writerow([
            project.id,
            project.name,
            project.description or 'No description',
            project.department.name,
            project.manager.get_full_name() if project.manager else 'Not assigned',
            project.status,
            project.start_date,
            project.end_date or 'Ongoing',
            'Yes' if project.is_active else 'No'
        ])
    
    return response