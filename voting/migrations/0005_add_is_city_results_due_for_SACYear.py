# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-22 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_winner_annoucement'),
    ]

    operations = [
        migrations.AddField(
            model_name='sacyear',
            name='alahsa_results_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0625\u0639\u0644\u0627\u0646 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0641\u064a \u0627\u0644\u0623\u062d\u0633\u0627\u0621'),
        ),
        migrations.AddField(
            model_name='sacyear',
            name='jeddah_results_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0625\u0639\u0644\u0627\u0646 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0641\u064a \u062c\u062f\u0629'),
        ),
        migrations.AddField(
            model_name='sacyear',
            name='riyadh_results_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0625\u0639\u0644\u0627\u0646 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0641\u064a \u0627\u0644\u0631\u064a\u0627\u0636'),
        ),
    ]
