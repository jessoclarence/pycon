# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 19:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0021_reg_conference_approve_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='reg_conference',
            name='approve_status',
            field=models.CharField(blank=True, choices=[('a', 'approved'), ('c', 'cancelled'), ('w', 'weightinglist'), ('y', 'yet to check')], default='y', help_text='status check', max_length=1),
        ),
    ]
