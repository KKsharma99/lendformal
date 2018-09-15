# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 03:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_item_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
