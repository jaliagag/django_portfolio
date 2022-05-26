from django.db import models

class Family_member(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth = models.DateField()
