from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.cla
class blog(models.Model):
    Name=models.CharField(max_length=100)


class blogcon(models.Model):
    title=models.CharField(max_length=100)
    date = models.DateField()
    Contents = models.CharField(max_length=200)
    is_publick = models.IntegerField()

class customuser(AbstractUser):
      pass



