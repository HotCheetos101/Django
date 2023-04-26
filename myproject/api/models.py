from django.db import models

# Create your models here.

class Profile(models.Model):
    last_name= models.CharField(max_length=100,null=True)
    first_name= models.CharField(max_length=100,null=True)
    