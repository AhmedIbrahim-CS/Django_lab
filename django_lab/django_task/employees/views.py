from django.shortcuts import render
from .models import Employee
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employees/employees.html', context={"employee": employee})


def employee_info(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    return render(request, 'employees/id.html', context={"employee": employee})
