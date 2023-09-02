#created a new urls.py file to define the urls.

from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('employees/<int:company_id>/', views.employee_list, name='employee_list'),
    path('devices/<int:company_id>/', views.device_list, name='device_list'),
    path('device/checkout/<int:device_id>/', views.device_checkout, name='device_checkout'),
    path('device/checkin/<int:device_id>/', views.device_checkin, name='device_checkin'),
    path('form-submissions/', views.form_submissions, name='form_submissions'),

]