from django import forms
from employeeReg import models

from .models import Employee


class Employee_form(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(Employee_form,self).__init__(*args,**kwargs)
        self.fields['Position'].empty_label="select"