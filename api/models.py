from django.conf import settings
from django.db import models

# Create your models here.


class Student(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    city=models.CharField(max_length=30)
    def __str__(self):
        return self.name