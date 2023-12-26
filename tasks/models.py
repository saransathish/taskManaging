from django.db import models
from datetime import date
# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)


class log(models.Model):
    active = models.BooleanField()
    username = models.CharField(max_length=255)


class toDoLists(models.Model):
    username = models.CharField(max_length=255)
    date = models.DateField(default=date.today)
    job = models.CharField(max_length=255)
    status = models.BooleanField()
    job_type = models.CharField(max_length=255)
