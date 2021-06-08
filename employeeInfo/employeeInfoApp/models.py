from django.db import models

class EmployeeDetails(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    job=models.CharField(max_length=50)
    salary=models.IntegerField()
    company=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    address=models.CharField(max_length=700)

