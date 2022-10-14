from django.db import models

# Create your models here.

class FileUpload(models.Model):
    coures = models.CharField(max_length=50, null = True)
    branch = models.CharField(max_length=50, null = True)
    year = models.IntegerField(default = 1, null = True)
    file = models.FileField(null = True)
    

class CreateAccounts(models.Model):
    studentPrn = models.IntegerField(null = False, blank=False, unique=True)
    studentName = models.CharField(max_length=50, null = False)
    studentEmail = models.EmailField(max_length=254)
    studentNumber = models.IntegerField(null = True, blank=False, unique=True)

class AdminAccounts(models.Model):
    adminName = models.CharField(max_length=50)
    adminEmail = models.EmailField(max_length=254, null = True)
    adminPassword = models.CharField(max_length=50)