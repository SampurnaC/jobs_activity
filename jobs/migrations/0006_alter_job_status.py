# Generated by Django 4.2.6 on 2023-11-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('Applied', 'APPLIED'), ('Interview', 'INTERVIEW'), ('Rejected', 'REJECTED'), ('Accepted', 'ACCEPTED')], default='applied', max_length=16),
        ),
    ]