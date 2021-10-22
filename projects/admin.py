from django.contrib import admin

# Register your models here.
# Once we have done the migrations, we have to reagiester it to the admin mode
from .models import Project
admin.site.register(Project)