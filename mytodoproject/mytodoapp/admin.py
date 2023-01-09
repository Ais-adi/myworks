from django.contrib import admin

# Register your models here.
from mytodoapp.models import task

admin.site.register(task)