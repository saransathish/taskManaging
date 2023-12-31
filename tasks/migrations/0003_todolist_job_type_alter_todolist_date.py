# Generated by Django 5.0 on 2023-12-26 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_log_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='job_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
