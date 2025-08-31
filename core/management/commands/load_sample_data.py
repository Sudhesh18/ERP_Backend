from django.core.management.base import BaseCommand
from core.models import Department, Employee, Project
from datetime import date

class Command(BaseCommand):
    help = 'Load sample dataset into the database'

    def handle(self, *args, **options):
        print('Loading sample data...')
    
        it_dept = Department.objects.create(name='IT', description='Technology Department')
        hr_dept = Department.objects.create(name='HR', description='Human Resources')
        finance_dept = Department.objects.create(name='Finance', description='Accounts Department')
   
        admin = Employee.objects.create(
            email='sudhesh418@gmail.com',
            first_name='Admin',
            last_name='User',
            employee_id='ADM001',
            department=it_dept,
            role='admin',
            salary=100000,
            is_staff=True,      
            is_superuser=True    
        )
        admin.set_password('admin123')
        admin.save()

   
        manager = Employee.objects.create(
            email='ravichandraa002@gmail.com',
            first_name='Ravi',
            last_name='Chandra', 
            employee_id='MGR001',
            department=hr_dept,
            role='manager',
            salary=80000,
            is_staff=True    
        )
        manager.set_password('manager123')
        manager.save()

 
        employee1 = Employee.objects.create(
            email='sakthivelsubash0402@gmail.com',  
            first_name='Sakthivel',
            last_name='Murugan',
            employee_id='EMP001',
            department=it_dept,
            role='employee',
            salary=50000
        )
        employee1.set_password('employee123')
        employee1.save()

        employee2 = Employee.objects.create(
            email='najith0421@gmail.com',
            first_name='Ajith',
            last_name='Kumar',
            employee_id='EMP002',
            department=hr_dept,
            role='employee',
            salary=45000
        )
        employee2.set_password('employee123')
        employee2.save()

    
        Project.objects.create(
            name='Website Project',
            description='Company website development',
            department=it_dept,
            manager=manager,
            start_date=date(2024, 1, 1),
            end_date=date(2024, 6, 1),
            status='in_progress',
            is_active=True
        )

        Project.objects.create(
            name='HR System',
            description='HR management system',
            department=hr_dept,
            manager=manager, 
            start_date=date(2024, 2, 1),
            status='planned',
            is_active=True
        )

        print('Sample data stored successfully!')
        print('You can now login with:')
        print('Admin: sudhesh418@gmail.com / admin123')
        print('Manager: ravichandraa002@gmail.com / manager123') 
        print('Employee: sakthivelsubash0402@gmail.com / employee123')  