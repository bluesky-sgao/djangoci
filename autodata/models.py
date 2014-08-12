from django.db import models
from django.contrib import admin

# Create your models here.
class AutoData(models.Model):
    data_name = models.CharField(max_length=150)
    data_value_1 = models.CharField(max_length=150)
    data_value_2 = models.CharField(max_length=150)
    data_value_3 = models.CharField(max_length=150)
    data_value_4 = models.CharField(max_length=150)
    data_value_5 = models.CharField(max_length=150)

class AutoData_Admin(admin.ModelAdmin):
    list_display = ('data_name', 'data_value_1', 'data_value_2', 'data_value_3', 'data_value_4', 'data_value_5')

class Meta:
    ordering = ('-timestamp',)

admin.site.register(AutoData, AutoData_Admin)
