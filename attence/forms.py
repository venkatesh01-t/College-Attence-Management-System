from .models import *
from django.forms import *
# myapp/forms.py
from django import forms

class CreateDepartmentForm(forms.Form):
    department_name = forms.CharField(label='Department Name', max_length=100)
    department_type = forms.CharField(label='Department Type', max_length=100)
