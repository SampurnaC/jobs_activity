# Generated by Django 4.2.6 on 2023-12-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_job_companyname_alter_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.CharField(default='', max_length=500),
        ),
    ]
