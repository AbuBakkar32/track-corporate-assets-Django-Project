from django.contrib import admin
from django.urls import path
from corporateAssetsTracker import views
from .views import (CompanyCreateView, CompanyListView, CompanyUpdateView, CompanyDeleteView,
                    EmployeeCreateView, EmployeeListView, EmployeeUpdateView, EmployeeDeleteView,
                    DeviceCreateView, DeviceListView, DeviceUpdateView, DeviceDeleteView,
                    DeviceLogCreateView, DeviceLogListView, DeviceLogUpdateView, DeviceLogDeleteView,
                    DeviceLogHistoryView, DeviceConditionLogCreateView, DeviceConditionLogListView,
                    DeviceConditionLogUpdateView, DeviceConditionLogDeleteView)

urlpatterns = [
    path('', views.index, name='index'),

    # Company URLs
    path('company/add/', CompanyCreateView.as_view(), name='company_add'),
    path('company/list/', CompanyListView.as_view(), name='company_list'),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),

    # Employee URLs
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/list/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),

    # Device URLs
    path('device/add/', DeviceCreateView.as_view(), name='device_add'),
    path('device/list/', DeviceListView.as_view(), name='device_list'),
    path('device/<int:pk>/update/', DeviceUpdateView.as_view(), name='device_update'),
    path('device/<int:pk>/delete/', DeviceDeleteView.as_view(), name='device_delete'),

    # DeviceLog URLs
    path('devices/logs/create/', DeviceLogCreateView.as_view(), name='device_log_create'),
    path('devices/logs/', DeviceLogListView.as_view(), name='device_log_list'),
    path('devices/logs/<int:pk>/update/', DeviceLogUpdateView.as_view(), name='device_log_update'),
    path('devices/logs/<int:pk>/delete/', DeviceLogDeleteView.as_view(), name='device_log_delete'),
    path('companies/<int:company_id>/devices/logs/', DeviceLogHistoryView.as_view(),
         name='company_device_logs_list'),

    # DeviceConditionLog URLs
    path('condition-log/create/', DeviceConditionLogCreateView.as_view(), name='device_condition_log_create'),
    path('condition-log/list/', DeviceConditionLogListView.as_view(), name='device_condition_log_list'),
    path('condition-log/<int:pk>/update/', DeviceConditionLogUpdateView.as_view(), name='device_condition_log_update'),
    path('condition-log/<int:pk>/delete/', DeviceConditionLogDeleteView.as_view(), name='device_condition_log_delete'),
]
