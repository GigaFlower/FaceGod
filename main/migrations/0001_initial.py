# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-31 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('file_name', models.CharField(max_length=100)),
            ],
        ),
    ]
