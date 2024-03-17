from .models import Job, Yo
from django.http import HttpResponse
import csv
import pandas as pd
from celery import shared_task
from django.conf import settings
# @shared_task(bind=True)
# def test_func(self):
#     for i in range(10):
#         print(i)
#     return "Coming from tasks.py"

@shared_task(bind=True)
def export(request, user_id):
    
    # current_user=request.user
    # jobs = Job.objects.filter(author_id=current_user.id).order_by('-created_at')


    # jobs=Yo.objects.all()
    # response = HttpResponse('text/csv')
    # response['Content-Disposition'] = 'attachment; filename=jobs_export.csv'
    # writer = csv.writer(response)
    # writer.writerow(['Name'])
    # jobs_fields = jobs.values_list('name')
    # for job in jobs_fields:
    #     writer.writerow(job)
    # return response
    # current_user=request.user.id
    objs = Job.objects.filter(author_id=user_id).order_by('-created_at')
    # objs=Yo.objects.all()
    payload = []

    for obj in objs:
        payload.append({
            'Position': obj.title,
            'Company Name': obj.companyname,
            'Status': obj.status,
            'URL': obj.url,

        })
    df = pd.DataFrame(payload)
    df.to_csv(f"yoman1", encoding='UTF-8')
