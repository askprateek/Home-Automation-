# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fan_id', models.PositiveSmallIntegerField()),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Led',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('led_id', models.PositiveSmallIntegerField()),
                ('status', models.BooleanField(default=0)),
            ],
        ),
    ]
