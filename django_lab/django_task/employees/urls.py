from django.urls import path
from employees.views import employee_list, employee_info
urlpatterns = [

path('index/', employee_list, name="all_employees" ),
path('<int:employee_id>/', employee_info, name="info" )

]




