# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winit', '0002_auto_20151126_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winit',
            name='confirmpassword',
        ),
        migrations.AlterField(
            model_name='winit',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
