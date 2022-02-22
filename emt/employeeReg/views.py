from django.shortcuts import render, redirect

# Create your views here.
from .forms import Employee_form
from .models import Employee


def employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'employee_list.html',context)


def employee_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form = Employee_form()
        else:
            employee=Employee.objects.get(pk=id)
            form= Employee_form(instance=employee)




        return render(request, 'employee_form.html', {'form': form})
    else:
        if id==0:
            form = Employee_form(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form=Employee_form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')






def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()

    return redirect('/list')
