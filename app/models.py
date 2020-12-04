from django.db import models


# Create your models here.


class User(models.Model):
    
    Name=models.CharField(max_length=20)
    Email=models.CharField(primary_key=True,max_length=30)
    Password=models.CharField(max_length=30)
    def __str__(self):
        return self.Name
