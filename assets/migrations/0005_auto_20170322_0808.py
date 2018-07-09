# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20170322_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='assets',
        ),
        migrations.AddField(
            model_name='asset',
            name='portfolios',
            field=models.ManyToManyField(to='assets.Portfolio'),
        ),
    ]