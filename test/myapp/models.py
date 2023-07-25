# models.py
from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_details = models.TextField()

    def __str__(self):
        return self.company_name

class Owner(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    owner_details = models.TextField()

    def __str__(self):
        return self.owner_name

class Employee(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    employee_details = models.TextField()

    def __str__(self):
        return self.employee_name

class Intern(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    intern_name = models.CharField(max_length=100)
    intern_details = models.TextField()

    def __str__(self):
        return self.intern_name
