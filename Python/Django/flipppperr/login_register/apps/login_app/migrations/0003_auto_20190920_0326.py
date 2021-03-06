# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-20 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20190920_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fav_books',
        ),
        migrations.AddField(
            model_name='book',
            name='fav_books',
            field=models.ManyToManyField(related_name='fans', to='login_app.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default='default user', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='login_app.User'),
            preserve_default=False,
        ),
    ]
