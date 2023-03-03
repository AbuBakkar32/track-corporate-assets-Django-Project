from django.test import TestCase
from django.urls import reverse
from .models import Company, Employee
from .views import CompanyUpdateView


class CompanyUpdateViewTestCase(TestCase):
    """
    In the setUp method, we create a test client,
    a Company object, the URL for the CompanyUpdateView,
    and the data we will use to update the company.
    """

    def setUp(self):
        self.company = Company.objects.create(name='Test Company', address='Test address')
        self.url = reverse('company_update', kwargs={'pk': self.company.pk})
        self.data = {'name': 'New Test Company', 'address': 'New Test address'}

    """
    The test_company_update_view_get method tests that
     we can successfully retrieve the CompanyUpdateView, 
     that the correct template is used, and that the response 
     contains the correct information for the Company object.
    """

    def test_company_update_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company_update.html')
        self.assertContains(response, 'Test Company')
        self.assertContains(response, 'Test address')

    """
    The test_company_update_view_post method tests that 
    we can successfully update the Company object by making a 
    POST request with the updated data, that the response is a redirect to the CompanyListView, 
    and that the Company object has been updated in the database with the new data.
    """

    def test_company_update_view_post(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('company_list'))
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, 'New Test Company')
        self.assertEqual(self.company.address, 'New Test address')


class CompanyListViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('company_list')
        self.company = Company.objects.create(name='Test Company')

    def test_company_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.company.name)

    def test_company_list_view_empty(self):
        Company.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No companies found.')


class EmployeeListViewTestCase(TestCase):
    """Test suite for the EmployeeListView"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.company = Company.objects.create(name='Test Company')
        self.employee1 = Employee.objects.create(name='Abu Bakkar', company=self.company)
        self.employee2 = Employee.objects.create(name='Bakkar Abu', company=self.company)

    def test_get_all_employees(self):
        """Test getting all employees"""
        response = self.client.get(reverse('employee_list'))
        employees = Employee.objects.all()
        serializer_data = EmployeeSerializer(employees, many=True).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_detail(self):
        """Test getting a single employee's details"""
        response = self.client.get(reverse('employee_detail', kwargs={'pk': self.employee1.pk}))
        employee = Employee.objects.get(pk=self.employee1.pk)
        serializer_data = EmployeeSerializer(employee).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        """Test creating a new employee"""
        data = {'name': 'Abu Bakkar', 'company': self.company.pk}
        response = self.client.post(reverse('employee_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_employee(self):
        """Test updating an existing employee"""
        data = {'name': 'Bakkar Abu', 'company': self.company.pk}
        response = self.client.put(reverse('employee_update', kwargs={'pk': self.employee1.pk}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        """Test deleting an existing employee"""
        response = self.client.delete(reverse('employee_delete', kwargs={'pk': self.employee1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
