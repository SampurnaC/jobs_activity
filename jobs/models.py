from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = (
    ('Applied', 'APPLIED'),
    ('Interview', 'INTERVIEW'),
    ('Rejected', 'REJECTED'),
    ('Accepted', 'ACCEPTED'),

)
class Job(models.Model):
    title = models.CharField(max_length=80)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    companyname = models.CharField(max_length=80, default='')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='applied')
    url = models.TextField(max_length=800, default='')
    extra_note = models.TextField(max_length=800, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
