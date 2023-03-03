from django.db import models
from django.utils import timezone


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "{'name':'''%s''', 'address':'''%s'''}" % (self.name, self.address)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{'name':'''%s''', 'company':'''%s'''}" % (self.name, self.company)


class Device(models.Model):
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{'name':'''%s''', 'condition':'''%s''', 'company':'''%s''','employee':'''%s''',}" % (
            self.name, self.condition, self.company, self.employee)


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=50)
    condition_when_checked_in = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{'device':'''%s''', 'check_out_time':'''%s''','check_in_time':'''%s''', 'condition_when_checked_out':'''%s''', 'condition_when_checked_in':'''%s''',}" % (
            self.device, self.check_out_time, self.check_in_time, self.condition_when_checked_out,
            self.condition_when_checked_in)


class DeviceConditionLog(models.Model):
    device_log = models.ForeignKey(DeviceLog, on_delete=models.CASCADE)
    condition = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
