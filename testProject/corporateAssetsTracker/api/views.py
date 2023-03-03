from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from corporateAssetsTracker.models import Company, Employee, Device, DeviceLog
from corporateAssetsTracker.api.serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, \
    DeviceLogSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceLogList(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer


class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer


# Here is the example of API view
@api_view(['POST'])
def add_employees(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    employee_data = request.data.get('employees', [])
    employees = []
    for emp in employee_data:
        emp['company'] = company.id
        serializer = EmployeeSerializer(data=emp)
        if serializer.is_valid():
            employees.append(serializer.save())

    return Response(EmployeeSerializer(employees, many=True).data, status=status.HTTP_201_CREATED)


"""
Response will be

{
    "employees": [
        {
            "name": "John Smith",
            "email": "john@example.com",
            "phone": "555-1234"
        },
        {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "555-5678"
        }
    ]
}

"""
