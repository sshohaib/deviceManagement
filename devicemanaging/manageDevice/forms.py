#creating new form for check in - check out.
from django import forms
from .models import Employee, Device

class DeviceLogForm(forms.Form):
    employee = forms.ModelChoiceField(
        queryset = Employee.objects.all(),
        empty_label = "Select an employee",
        widget = forms.Select(attrs={'class': 'form-control'})
    )
    checkout_condition = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'form-control'}),
        required = False
    )
    return_condition = forms.CharField(
        widget = forms.Textarea(attrs={'class': 'form-control'}),
        required = False
    )