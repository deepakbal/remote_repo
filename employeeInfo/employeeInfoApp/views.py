from django.shortcuts import render
from django.http.response import HttpResponse
import faker
from .models import EmployeeDetails
fake = faker.Faker()

def employeedata(request):
  for i in range(10):
      first_name=fake.first_name()
      last_name=fake.last_name()
      email=fake.email()
      job=fake.random_element(elements=('software','Trainer','govt','defence','hardware'))
      salary=fake.random_element(elements=(2000,500000,753652,78945,3654))
      company=fake.random_element(elements=('TCS','Infosis','mindtree','cognijant'))
      location=fake.random_element(elements=('HYD','CHENNAI','BENGALURU','BBSR'))
      address=fake.address()

      EmployeeDetails(
          first_name=first_name,
          last_name=last_name,
          email=email,
          job=job,
          salary=salary,
          company=company,
          location=location,
          address=address
       ).save()
  return HttpResponse('Data saved')

def fetch_data(request):
    employees=EmployeeDetails.objects.all()
    return render(request,'employeedata.html',{'employees':employees})

def home(request):
    return render(request,'home.html')


def hyd_data(request):
    employees= EmployeeDetails.objects.filter(location='HYD')
    return render(request,'employee_hyd.html',{'employees':employees})


def chennai_data(request):
    employees=EmployeeDetails.objects.filter(location='CHENNAI')
    return render(request,'employee_chennai.html',{'employees':employees})


def benaluru_data(request):
    employees=EmployeeDetails.objects.filter(location='BENGALURU')
    return render(request,'employee_bengaluru.html',{'employees':employees})


def bbsr_data(request):
    employees=EmployeeDetails.objects.filter(location='BBSR')

    return render(request,'employee_bbsr.html',{'employees':employees})