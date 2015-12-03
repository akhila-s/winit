# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('winit', '0005_auto_20151201_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 15, 22, 52, 363000)),
        ),
    ]
