# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0008_aceuserprofile_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aceuserprofile',
            name='course',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]