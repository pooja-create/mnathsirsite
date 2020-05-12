from django.contrib import admin

# Register your models here.
from .models import job
from .models import categorytable
admin.site.register(job)
admin.site.register(categorytable)
