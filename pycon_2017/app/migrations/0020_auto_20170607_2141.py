# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 21:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20170606_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_conference',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
