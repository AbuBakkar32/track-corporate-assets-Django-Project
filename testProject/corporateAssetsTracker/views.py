from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Company, Employee, Device, DeviceLog, DeviceConditionLog
from .forms import CompanyForm, EmployeeForm, DeviceForm, DeviceLogForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


def index(request):
    return HttpResponse("Thank You For Visit Assets Tracker")


# START--Company Model Related Functionalities
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'add_company.html'
    success_url = reverse_lazy('company_list')


class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'companies'


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'edit_company.html'
    success_url = reverse_lazy('company_list')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'delete_company.html'
    success_url = reverse_lazy('company_list')


# END--Company Model Related Functionalities


# START--Employee Model Related Functionalities
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        company_id = self.kwargs['company_id']
        company = get_object_or_404(Company, id=company_id)
        kwargs['initial']['company'] = company
        return kwargs

    def get_success_url(self):
        return reverse_lazy('employee_list', kwargs={'company_id': self.kwargs['company_id']})


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'update_employee.html'
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'delete_employee.html'
    success_url = reverse_lazy('employee_list')


# END--Employee Model Related Functionalities


# START--Device Model Related Functionalities
class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'add_device.html'
    success_url = reverse_lazy('device_list')

    def form_valid(self, form):
        # set the company for the device based on the logged in user's company
        form.instance.company = self.request.user.employee.company
        return super().form_valid(form)


class DeviceListView(ListView):
    model = Device
    template_name = 'device_list.html'
    context_object_name = 'devices'

    def get_queryset(self):
        # only show devices for the logged in user's company
        return Device.objects.filter(company=self.request.user.employee.company)


class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'update_device.html'
    success_url = reverse_lazy('device_list')

    def get_queryset(self):
        # only allow editing devices for the logged in user's company
        return Device.objects.filter(company=self.request.user.employee.company)


class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'delete_device.html'
    success_url = reverse_lazy('device_list')

    def get_queryset(self):
        # only allow deleting devices for the logged in user's company
        return Device.objects.filter(company=self.request.user.employee.company)


# END--Device Model Related Functionalities


# START--DeviceLog Model Related Functionalities
class DeviceLogCreateView(CreateView):
    model = DeviceLog
    fields = ['device', 'employee', 'checked_out_date', 'checked_in_date', 'condition']
    success_url = reverse_lazy('device_log_list')

    def form_valid(self, form):
        # Set the company of the device based on the assigned employee
        employee = form.cleaned_data.get('employee')
        if employee:
            form.instance.company = employee.company
        return super().form_valid(form)


class DeviceLogListView(ListView):
    model = DeviceLog
    template_name = 'device_log_list.html'
    context_object_name = 'logs'


class DeviceLogUpdateView(UpdateView):
    model = DeviceLog
    template_name = 'edit_device_log.html'
    fields = ['device', 'employee', 'checkout_date', 'return_date', 'condition']
    success_url = reverse_lazy('device_log_list')


class DeviceLogDeleteView(DeleteView):
    model = DeviceLog
    template_name = 'delete_device_log.html'
    success_url = reverse_lazy('device_log_list')

    def get_queryset(self):
        # only allow deleting devices for the logged in user's company
        return DeviceLog.objects.filter(company=self.request.user.employee.company)


# END--DeviceLog Model Related Functionalities


# START--Here is the code for where "Each company able to see when a Device was checked out and returned"
class DeviceLogHistoryView(ListView):
    template_name = 'device_log_history.html'
    context_object_name = 'device_log_list'

    def get_queryset(self):
        company = get_object_or_404(Company, pk=self.kwargs['company_pk'])
        device = get_object_or_404(Device, pk=self.kwargs['device_pk'])
        device_logs = DeviceLog.objects.filter(company=company, device=device).order_by('-checked_out_date')
        return device_logs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = get_object_or_404(Company, pk=self.kwargs['company_pk'])
        device = get_object_or_404(Device, pk=self.kwargs['device_pk'])
        context['company'] = company
        context['device'] = device
        return context


# END--Here is the code for where "Each company able to see when a Device was checked out and returned"


# START--Here is the code for where "Each device should have a log of what condition it was handed out and returned"

class DeviceConditionLogCreateView(CreateView):
    model = DeviceConditionLog
    fields = ['condition']
    template_name = 'device_condition_log_form.html'

    def form_valid(self, form):
        device_log_id = self.kwargs.get('device_log_id')
        device_log = get_object_or_404(DeviceLog, id=device_log_id)
        self.object = form.save(commit=False)
        self.object.device_log = device_log
        self.object.save()
        return super().form_valid(form)


class DeviceConditionLogListView(ListView):
    model = DeviceConditionLog
    template_name = 'device_condition_log_list.html'

    def get_queryset(self):
        device_log_id = self.kwargs.get('device_log_id')
        device_log = get_object_or_404(DeviceLog, id=device_log_id)
        queryset = super().get_queryset().filter(device_log=device_log)
        return queryset


class DeviceConditionLogUpdateView(UpdateView):
    model = DeviceConditionLog
    fields = ['condition']
    template_name = 'device_condition_log_form.html'


class DeviceConditionLogDeleteView(DeleteView):
    model = DeviceConditionLog
    template_name = 'device_condition_log_confirm_delete.html'
    success_url = reverse_lazy('device_log_list')

# END--Here is the code for where "Each device should have a log of what condition it was handed out and returned"
