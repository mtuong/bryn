# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('userdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='group',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
    ]
