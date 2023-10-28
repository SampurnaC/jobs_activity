from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=90)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    companyname = models.CharField(max_length=90, default='')
    url = models.CharField(max_length=90, default='')

    def __str__(self):
        return self.title
