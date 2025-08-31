from rest_framework import serializers
from .models import Department, Employee, Project

class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'employee_count', 'total_salary']

    def get_employee_count(self, obj):
        return obj.employees.count()

    def get_total_salary(self, obj):
        total = 0
        for employee in obj.employees.all():
            total += employee.salary
        return total


class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'email', 'first_name', 'last_name', 'employee_id', 
                 'department', 'department_name', 'role', 'salary', 'hire_date', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        employee = Employee.objects.create(**validated_data)
        if password:
            employee.set_password(password)
            employee.save()
        return employee


class ProjectSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    manager_name = serializers.CharField(source='manager.get_full_name', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'department', 'department_name', 
                 'manager', 'manager_name', 'start_date', 'end_date', 'status', 'is_active']