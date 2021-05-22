from django.contrib import admin
from .models import TestModel, ModelX

# Register your models here.

admin.site.register((TestModel, ModelX))