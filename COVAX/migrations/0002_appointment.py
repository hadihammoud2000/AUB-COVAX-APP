# Generated by Django 3.0.1 on 2021-11-20 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('COVAX', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dose', models.CharField(max_length=40)),
                ('Dose_one_date', models.DateTimeField(auto_now=True, null=True)),
                ('Dose_two_date', models.DateTimeField(null=True)),
                ('Patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='COVAX.PatientExtra')),
            ],
        ),
    ]
