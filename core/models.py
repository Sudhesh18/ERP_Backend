from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    def employee_count(self):
        return self.employees.count()


    def total_salary_cost(self):
        total = 0
        for employee in self.employees.all():
            total += employee.salary
        return total


class Employee(AbstractUser):
    Role = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    role = models.CharField(max_length=20, choices=Role, default='employee')
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    hire_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_admin_user(self):
        return self.role == 'admin'

    def is_manager_user(self):
        return self.role == 'manager'


class Project(models.Model):
    status = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_projects')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status, default='planned')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_employees = models.ManyToManyField(Employee,related_name='assigned_projects',blank=True)


    def __str__(self):
        return self.name

    def is_active_project(self):
        return self.is_active and self.status != 'completed'