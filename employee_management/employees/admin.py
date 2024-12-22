from django.contrib import admin

from .models import CustomUser, Project, Employee

admin.site.register(CustomUser)
admin.site.register(Project)    
admin.site.register(Employee)