from django.contrib import admin
from django.urls import path
import corporateAssetsTracker.views as views
import corporateAssetsTracker.api.views as api

urlpatterns = [
    path('', views.add_company, name='add_company'),

    # for API management URL
    path('companies/', api.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', api.CompanyDetail.as_view(), name='company-detail'),
    path('employees/', api.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', api.EmployeeDetail.as_view(), name='employee-detail'),
    path('devices/', api.DeviceList.as_view(), name='device-list'),
    path('devices/<int:pk>/', api.DeviceDetail.as_view(), name='device-detail'),
    path('devicelogs/', api.DeviceLogList.as_view(), name='devicelog-list'),
    path('devicelogs/<int:pk>/', api.DeviceLogDetail.as_view(), name='devicelog-detail'),
]
