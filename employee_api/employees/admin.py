from django.contrib import admin

from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','role','department','date_joined')
    search_fields = ('name','email')