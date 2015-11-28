# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winit',
            old_name='first_name',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='winit',
            old_name='last_name',
            new_name='Lastname',
        ),
        migrations.RenameField(
            model_name='winit',
            old_name='confirm_password',
            new_name='confirmpassword',
        ),
        migrations.RenameField(
            model_name='winit',
            old_name='contact_number',
            new_name='contactnumber',
        ),
    ]
