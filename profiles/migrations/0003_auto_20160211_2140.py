# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-02-11 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profiles',
            new_name='profile',
        ),
    ]
