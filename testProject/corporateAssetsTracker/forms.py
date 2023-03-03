from django import forms
from corporateAssetsTracker.models import Company, Employee, Device, DeviceLog

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'company']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'condition', 'company', 'employee']

class DeviceLogForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['device', 'check_in_time', 'condition_when_checked_out', 'condition_when_checked_in']
