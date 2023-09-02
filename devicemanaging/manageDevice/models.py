from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.TextField()
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name
    

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField()
    return_time = models.DateTimeField()
    checkout_condition = models.TextField()
    return_condition = models.TextField()

    def __str__(self):
        return f"{self.device.name} - {self.employee.name}"