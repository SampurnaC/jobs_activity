# Generated by Django 4.2.6 on 2023-11-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_job_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='companyname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]