from django.db import models
# from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('Applied', 'APPLIED'),
    ('Interview', 'INTERVIEW'),
    ('Rejected', 'REJECTED'),
    ('Accepted', 'ACCEPTED'),

)
class Job(models.Model):
    title = models.CharField(max_length=80)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    companyname = models.CharField(max_length=80, default='')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='applied')
    url = models.TextField(max_length=800, default='')
    extra_note = models.TextField(max_length=800, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", default=1)

    def __str__(self):
        return self.title
