from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=50)
    condition_when_checked_in = models.CharField(max_length=50, null=True, blank=True)
