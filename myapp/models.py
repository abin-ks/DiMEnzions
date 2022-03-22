from django.db import models

# Create your models here.

class Admin_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    joining_date= models.DateTimeField(null=True,blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    
    