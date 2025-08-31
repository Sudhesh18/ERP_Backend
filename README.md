# ERP Backend System

A comprehensive Django REST Framework backend for an Enterprise Resource Planning (ERP) system that manages Employees, Departments, and Projects with role-based access control.

## 🚀 Features

- **Role-Based Authentication** (Admin, Manager, Employee)
- **Complete CRUD Operations** for all entities
- **RESTful API** with Django REST Framework
- **Business Intelligence Reports**
- **CSV Export Functionality** (Bonus feature)
- **Django Admin Interface**
- **Email-based Authentication** (no username required)

## 📋 API Endpoints

### Authentication
- Uses Basic Authentication with email and password
- Role-based permissions for all operations

### Core Entities
| Method | Endpoint | Description | Access |
|--------|----------|-------------|---------|
| GET | `/api/departments/` | List all departments | All authenticated |
| POST | `/api/departments/` | Create new department | Admin, Manager |
| GET | `/api/departments/{id}/` | Get department details | All authenticated |
| PUT | `/api/departments/{id}/` | Update department | Admin, Manager |
| DELETE | `/api/departments/{id}/` | Delete department | Admin, Manager |

| Method | Endpoint | Description | Access |
|--------|----------|-------------|---------|
| GET | `/api/employees/` | List all employees | All authenticated |
| POST | `/api/employees/` | Create new employee | Admin only |
| GET | `/api/employees/{id}/` | Get employee details | All authenticated |
| PUT | `/api/employees/{id}/` | Update employee | Admin only |
| DELETE | `/api/employees/{id}/` | Delete employee | Admin only |

| Method | Endpoint | Description | Access |
|--------|----------|-------------|---------|
| GET | `/api/projects/` | List all projects | All authenticated |
| POST | `/api/projects/` | Create new project | Admin, Manager |
| GET | `/api/projects/{id}/` | Get project details | All authenticated |
| PUT | `/api/projects/{id}/` | Update project | Admin, Manager |
| DELETE | `/api/projects/{id}/` | Delete project | Admin, Manager |

### Reports & Analytics
| Method | Endpoint | Description | Access |
|--------|----------|-------------|---------|
| GET | `/api/reports/employees-by-department/` | Employee count by department | All authenticated |
| GET | `/api/reports/salary-cost/` | Salary expenditure by department | All authenticated |
| GET | `/api/reports/active-projects/` | List of active projects | All authenticated |

### Export Endpoints
| Method | Endpoint | Description | Access |
|--------|----------|-------------|---------|
| GET | `/api/export/employees-csv/` | Export employees to CSV | Admin, Manager |
| GET | `/api/export/departments-csv/` | Export departments to CSV | Admin, Manager |
| GET | `/api/export/projects-csv/` | Export projects to CSV | Admin, Manager |

## 🛠️ Technology Stack

- **Backend Framework**: Django 4.2+
- **REST API**: Django REST Framework
- **Database**: SQLite (can be configured for PostgreSQL/MySQL)
- **Authentication**: Django Auth with custom User model
- **Validation**: Django validators and DRF serializers

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Sudhesh18/ERP_Backend.git
cd erp-backend