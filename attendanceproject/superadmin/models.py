from django.db import models

# Create your models here.

class FileUpload(models.Model):
    coures = models.CharField(max_length=50, null = True)
    branch = models.CharField(max_length=50, null = True)
    year = models.IntegerField(default = 1, null = True)
    file = models.FileField(null = True)

# class MakePanels(models.Model):
#     year = models.CharField(max_length=50, null = True)
#     course = models.CharField(max_length=50, null = True)

#     def __str__(self):
#         return self.year
    