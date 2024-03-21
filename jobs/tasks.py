from .models import Job
from django.http import HttpResponse
import os
import csv
import pandas as pd
# from celery import shared_task
from django.conf import settings

# @shared_task(bind=True)
# def export(request, user_id):
    
#     objs = Job.objects.filter(author_id=user_id).order_by('-created_at')
#     payload = []
#     for obj in objs:
#         payload.append({
#             'Position': obj.title,
#             'Company Name': obj.companyname,
#             'Status': obj.status,
#             'URL': obj.url,

#         })
#     df = pd.DataFrame(payload)

#     downloads_folder = os.path.expanduser("~/Downloads")
    
#     file_path = os.path.join(downloads_folder, 'AllJobs.csv')

#     df.to_csv(file_path, index=False)

