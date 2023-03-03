from rest_framework import serializers
from corporateAssetsTracker.models import Company, Employee, Device, DeviceLog

"""
Here is the basic Serializers class. 
As per the customer need will able to modify the classes
"""


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Device
        fields = '__all__'


class DeviceLogSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    device = DeviceSerializer()

    class Meta:
        model = DeviceLog
        fields = '__all__'
