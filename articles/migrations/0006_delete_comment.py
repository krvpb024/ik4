# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160624_0627'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]