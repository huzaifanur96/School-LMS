# Generated by Django 2.1 on 2019-03-14 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('registrationNo', models.AutoField(primary_key=True, serialize=False)),
                ('fatherName', models.CharField(blank=True, max_length=200, null=True)),
                ('birthDay', models.DateField(default=datetime.date.today)),
                ('password', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('course', models.ManyToManyField(related_name='students', to='course.Course')),
            ],
        ),
    ]
