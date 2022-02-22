
from django.contrib import admin
from django.urls import path

from employeeReg.views import employee_list, employee_form, employee_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',employee_list,name='employeeList'),
    path('form/',employee_form,name='employeeInsert'),
    path('delete/<int:id>',employee_delete,name='employeeDelete'),
    path('<int:id>',employee_form,name='employeeUpdate')
]