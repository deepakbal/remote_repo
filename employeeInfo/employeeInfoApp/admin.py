from django.contrib import admin
from .models import EmployeeDetails

class AdminmEmployeeDetails(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','job','salary','company','location']
admin.site.register(EmployeeDetails,AdminmEmployeeDetails)

