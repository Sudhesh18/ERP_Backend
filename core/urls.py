from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports/employees-by-department/', views.employees_by_department),
    path('reports/salary-cost/', views.salary_cost_per_department),
    path('reports/active-projects/', views.active_projects_list),
    
    path('export/employees-csv/', views.export_employees_csv, name='export-employees-csv'),
    path('export/departments-csv/', views.export_departments_csv, name='export-departments-csv'),
    path('export/projects-csv/', views.export_projects_csv, name='export-projects-csv'),
]