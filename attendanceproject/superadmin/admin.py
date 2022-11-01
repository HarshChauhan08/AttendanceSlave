from django.contrib import admin
from .models import * 

# Register your models here.
# class MakePanels(admin.ModelAdmin):
#     list_display = ['id', 'year', 'course']

@admin.register(FileUpload)
class FileUpload(admin.ModelAdmin):
    list_display = ['coures', 'branch', 'year', 'file']

@admin.register(CreateAccounts)
class CreateAccounts(admin.ModelAdmin):
    list_display = ['studentPrn','studentName','studentEmail','studentNumber']

@admin.register(AdminAccount)
class AdminAccount(admin.ModelAdmin):
    list_display = ['AP_ID', 'adminName','adminEmail','adminPassword']
