from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Company, Employee, Device, DeviceLog
from .forms import DeviceLogForm
from datetime import datetime

# Create your views here.
# views.py

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def employee_list(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    employees = Employee.objects.filter(company=company)
    return render(request, 'employee_list.html', {'company': company, 'employees': employees})

def device_list(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    # Get all employees belonging to the company
    employees = Employee.objects.filter(company=company)
    
    # Get devices associated with those employees
    devices = Device.objects.filter(employee__in=employees)
    
    return render(request, 'device_list.html', {'company': company, 'devices': devices})


def device_checkout(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    
    if request.method == 'POST':
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            checkout_condition = form.cleaned_data['checkout_condition']
            
            # Set the checkout time to the current time
            checkout_time = datetime.now()
            
            # Create a DeviceLog entry for check-out
            log_entry = DeviceLog(
                device = device,
                employee = employee,
                checkout_time = checkout_time,  # Set the checkout time
                checkout_condition = checkout_condition
            )
            log_entry.save()
            
            # You can also update the device's status or availability here
            
            return redirect('device_list', company_id=device.company.id)
    else:
        form = DeviceLogForm()
    
    return render(request, 'device_checkout.html', {'device': device, 'form': form})

def device_checkin(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    
    if request.method == 'POST':
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            return_condition = form.cleaned_data['return_condition']
            
            # Find the most recent log entry for this device and employee
            log_entry = DeviceLog.objects.filter(device=device, employee=device.current_employee).latest('checkout_time')
            log_entry.return_condition = return_condition
            log_entry.save()
            
            return redirect('device_list', company_id=device.company.id)
    else:
        form = DeviceLogForm()
    
    return render(request, 'device_checkin.html', {'device': device, 'form': form})


def form_submissions(request):
    check_out_logs = DeviceLog.objects.filter(return_time__isnull=True)
    check_in_logs = DeviceLog.objects.exclude(return_time__isnull=True)
    return render(request, 'form_submissions_list.html', {'check_out_logs': check_out_logs, 'check_in_logs': check_in_logs})
