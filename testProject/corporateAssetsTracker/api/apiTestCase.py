from django.test import TestCase
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer


class CompanySerializerTestCase(TestCase):
    def setUp(self):
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
        self.company = Company.objects.create(name='ACME Corporation')
        self.employee = Employee.objects.create
