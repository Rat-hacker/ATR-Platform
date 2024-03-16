from django.db import models

# Create your models here.
class Login_Password(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=64)