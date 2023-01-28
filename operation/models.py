from django.db import models

# Create your models here.
class addmodel(models.Model):
    asnnumber=models.IntegerField()
    gsdb=models.CharField(max_length=5)
    supplier=models.CharField(max_length=5)
    date=models.DateTimeField()
    pknumber=models.IntegerField()
