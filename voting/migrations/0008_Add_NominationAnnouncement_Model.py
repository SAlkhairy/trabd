# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0007_nomination_gpa'),
    ]

    operations = [
    ]