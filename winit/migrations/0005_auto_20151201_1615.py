# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winit', '0004_auto_20151128_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=300, serialize=False, primary_key=True),
        ),
    ]
