# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-29 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_nomination_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomination',
            name='certificates',
        ),
        migrations.RemoveField(
            model_name='nomination',
            name='photo',
        ),
    ]
