from django.db import models
from django.core.validators import RegexValidator
from django.core import validators
# class User(models.Model):
#     alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
#     username=models.CharField(max_length=50,validators=[alpha])
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     email = models.EmailField(max_length=50,unique=True)
#     password = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     pincode=models.CharField(max_length=6)
class Person(models.Model):
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    p=RegexValidator()
    username=models.CharField(max_length=50,validators=[alpha])
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=15,validators=[RegexValidator(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}", message="Enter a Valid Indian password Number")])
    phone =models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)

# Create your models here.
