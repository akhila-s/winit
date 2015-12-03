# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winit', '0006_auto_20151202_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
