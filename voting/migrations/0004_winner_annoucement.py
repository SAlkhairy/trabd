# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 19:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0003_field_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnelectedWinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unelected_winner', to='voting.Position', verbose_name='\u0627\u0644\u0645\u0646\u0635\u0628')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u0640/\u0640\u0629')),
            ],
            options={
                'verbose_name': '\u0641\u0627\u0626\u0632/\u0629 \u062a\u0644\u0642\u0627\u0626\u064a\u064b\u0627',
                'verbose_name_plural': '\u0627\u0644\u0641\u0627\u0626\u0632\u0648\u0646/\u0627\u0644\u0641\u0627\u0626\u0632\u0627\u062a \u062a\u0644\u0642\u0627\u0626\u064a\u064b\u0627',
            },
        ),
        migrations.AddField(
            model_name='votenomination',
            name='is_counted',
            field=models.BooleanField(default=True),
        ),
    ]
