from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
