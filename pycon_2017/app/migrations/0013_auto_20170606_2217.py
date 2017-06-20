# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_reg_conference_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_conference',
            name='address',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_conference',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
