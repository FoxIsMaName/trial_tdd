# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 05:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find_your_cab', '0003_remove_cabuser_date_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabdriver',
            name='cab_user',
        ),
    ]
