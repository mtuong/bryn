# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('userdb', '0002_auto_20160711_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofile',
            name='department',
            field=models.CharField(max_length=50, verbose_name='Department or Institute'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='held_mrc_grants',
            field=models.TextField(help_text='If you currently or recent have held grant funding from the Medical Research Council it would be very helpful if you can detail it here to assist with reporting use of CLIMB', verbose_name='Held MRC grants'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='institution',
            field=models.CharField(max_length=100, verbose_name='Institution (e.g. University of St. Elsewhere)'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='intended_climb_use',
            field=models.TextField(help_text='Please let us know how you or your group intend to use CLIMB', verbose_name='Intended use of CLIMB'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='position',
            field=models.CharField(max_length=50, verbose_name='Position (e.g. Professor)'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='research_interests',
            field=models.TextField(help_text='Please supply a brief synopsis of your research programme', verbose_name='Research interests'),
        ),
    ]
