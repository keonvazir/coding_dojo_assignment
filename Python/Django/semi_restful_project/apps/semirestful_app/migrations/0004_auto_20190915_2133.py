# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-15 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semirestful_app', '0003_auto_20190915_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restful',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
