from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=90)
    companyname = models.CharField(max_length=90, default='')
    url = models.CharField(max_length=90, default='')

    def __str__(self):
        return self.title
