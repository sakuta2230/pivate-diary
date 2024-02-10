from django.db import models
class article(models.Model):
    title=models.CharField()
    text=models.TextField()
    date=models.DateField() 
# Create your models here.
