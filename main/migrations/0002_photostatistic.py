# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-01 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistic', models.CharField(max_length=500)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]