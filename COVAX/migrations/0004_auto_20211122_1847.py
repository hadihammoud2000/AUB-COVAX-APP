# Generated by Django 3.0.1 on 2021-11-22 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COVAX', '0003_auto_20211120_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Dose_one_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 8, 0)),
        ),
    ]
