from django.db import models  #importo modelos del fatabas
from datetime import datetime

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthday = models.DateField(blank=True, null=True, verbose_name="DOB" )  
    # adult = models.BooleanField()
    # email = models.EmailField()

