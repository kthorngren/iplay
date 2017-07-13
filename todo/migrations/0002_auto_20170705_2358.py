# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 23:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='todo_job',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 23, 58, 15, 616253), editable=False),
        ),
    ]
