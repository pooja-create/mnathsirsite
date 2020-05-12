from django.contrib import admin

# Register your models here.
from .models import categorytable
from .models import development
admin.site.register(development)
admin.site.register(categorytable)