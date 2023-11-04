from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS_CHOICES = (
    ('Applied', 'APPLIED'),
    ('Interview', 'INTERVIEW'),
    ('Rejected', 'REJECTED'),
    ('Accepted', 'ACCEPTED'),

)
class Job(models.Model):
    title = models.CharField(max_length=50)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    companyname = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='applied')
    url = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.title
