# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170606_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_conference',
            name='pincode',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]