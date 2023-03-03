from django.test import TestCase
from datetime import datetime
from corporateAssetsTracker.models import Company, Employee, Device, DeviceLog
from corporateAssetsTracker.api.serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, \
    DeviceLogSerializer
from rest_framework.exceptions import ValidationError


# CompanySerializer TestCase
class CompanySerializerTestCase(TestCase):
    def setUp(self):
        """setup the common all of those instance,
        value or data which need to test for every function"""
        self.company = Company.objects.create(name='ACME Corporation')

    def test_company_serialization(self):
        serializer = CompanySerializer(instance=self.company)
        expected_data = {'id': self.company.id, 'name': 'ACME Corporation'}
        self.assertEqual(serializer.data, expected_data)

    def test_company_deserialization(self):
        data = {'name': 'Globex Corporation'}
        serializer = CompanySerializer(data=data)
        serializer.is_valid()
        company = serializer.save()
        self.assertEqual(company.name, 'Globex Corporation')


class EmployeeSerializerTestCase(TestCase):
    def setUp(self):
        """setup the common all of those instance,
                value or data which need to test for every function"""
        self.company = Company.objects.create(name='ACME Corporation')
        self.employee = Employee.objects.create(name='John Doe', email='johndoe@example.com', company=self.company)

    def test_employee_serialization(self):
        serializer = EmployeeSerializer(instance=self.employee)
        expected_data = {'id': self.employee.id, 'name': 'John Doe', 'email': 'johndoe@example.com',
                         'company': {'id': self.company.id, 'name': 'ACME Corporation'}}
        self.assertEqual(serializer.data, expected_data)

    def test_employee_deserialization(self):
        data = {'name': 'Jane Doe', 'email': 'janedoe@example.com', 'company': self.company.id}
        serializer = EmployeeSerializer(data=data)
        serializer.is_valid()
        employee = serializer.save()
        self.assertEqual(employee.name, 'Jane Doe')
        self.assertEqual(employee.email, 'janedoe@example.com')
        self.assertEqual(employee.company, self.company)


class DeviceSerializerTestCase(TestCase):
    def setUp(self):
        """setup the common all of those instance,
                value or data which need to test for every function"""
        self.company = Company.objects.create(name='ACME Corporation')
        self.device = Device.objects.create(name='Macbook Pro', company=self.company, description='A laptop')

    def test_device_serialization(self):
        serializer = DeviceSerializer(instance=self.device)
        expected_data = {'id': self.device.id, 'name': 'Macbook Pro', 'company': {'id': self.company.id,
                                                                                  'name': 'ACME Corporation'},
                         'description': 'A laptop'}
        self.assertEqual(serializer.data, expected_data)

    def test_device_deserialization(self):
        data = {'name': 'iPad', 'company': self.company.id, 'description': 'A tablet'}
        serializer = DeviceSerializer(data=data)
        serializer.is_valid()
        device = serializer.save()
        self.assertEqual(device.name, 'iPad')
        self.assertEqual(device.company, self.company)
        self.assertEqual(device.description, 'A tablet')


class DeviceLogSerializerTestCase(TestCase):
    def setUp(self):
        """setup the common all of those instance,
                value or data which need to test for every function"""
        self.company = Company.objects.create(name='ACME Corporation')
        self.employee = Employee.objects.create(name='John Smith', company=self.company)
        self.device = Device.objects.create(name='Macbook Pro', company=self.company, description='A laptop')
        self.device_log = DeviceLog.objects.create(employee=self.employee, device=self.device,
                                                   checked_out=datetime(2022, 1, 1, 12, 0, 0),
                                                   checked_in=datetime(2022, 1, 2, 12, 0, 0), condition='Good')

    def test_device_log_serialization(self):
        serializer = DeviceLogSerializer(instance=self.device_log)
        expected_data = {'id': self.device_log.id,
                         'employee': {'id': self.employee.id, 'name': 'John Smith',
                                      'company': {'id': self.company.id, 'name': 'ACME Corporation'}},
                         'device': {'id': self.device.id, 'name': 'Macbook Pro',
                                    'company': {'id': self.company.id, 'name': 'ACME Corporation'},
                                    'description': 'A laptop'},
                         'checked_out': '2022-01-01T12:00:00Z', 'checked_in': '2022-01-02T12:00:00Z',
                         'condition': 'Good'}
        self.assertEqual(serializer.data, expected_data)

    def test_device_log_deserialization(self):
        data = {'employee': self.employee.id, 'device': self.device.id,
                'checked_out': '2022-01-03T12:00:00Z', 'checked_in': '2022-01-04T12:00:00Z',
                'condition': 'Fair'}
        serializer = DeviceLogSerializer(data=data)
        serializer.is_valid()
        device_log = serializer.save()
        self.assertEqual(device_log.employee, self.employee)
        self.assertEqual(device_log.device, self.device)
        self.assertEqual(device_log.checked_out, datetime(2022, 1, 3, 12, 0, 0))
        self.assertEqual(device_log.checked_in, datetime(2022, 1, 4, 12, 0, 0))
        self.assertEqual(device_log.condition, 'Fair')

    def test_device_log_deserialization_with_invalid_data(self):
        data = {'employee': self.employee.id, 'device': self.device.id,
                'checked_out': '2022-01-03T12:00:00Z', 'checked_in': '2022-01-02T12:00:00Z',
                'condition': 'Fair'}
        serializer = DeviceLogSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
