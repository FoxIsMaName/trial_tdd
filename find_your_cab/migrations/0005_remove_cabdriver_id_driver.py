# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find_your_cab', '0004_remove_cabdriver_cab_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabdriver',
            name='id_driver',
        ),
    ]