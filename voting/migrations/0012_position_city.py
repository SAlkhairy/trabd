# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0011_remove_certificates_nomination_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='city',
            field=models.CharField(blank=True, choices=[('R', '\u0627\u0644\u0631\u064a\u0627\u0636'), ('J', '\u062c\u062f\u0629'), ('A', '\u0627\u0644\u0623\u062d\u0633\u0627\u0621')], default='', max_length=1, verbose_name='\u0627\u0644\u0645\u062f\u064a\u0646\u0629'),
        ),
    ]