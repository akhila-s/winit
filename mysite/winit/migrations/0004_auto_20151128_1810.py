# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winit', '0003_auto_20151127_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('queno', models.IntegerField(serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('Firstname', models.CharField(max_length=30, null=True, blank=True)),
                ('Lastname', models.CharField(max_length=30, null=True, blank=True)),
                ('dateofbirth', models.DateField(max_length=30, null=True, blank=True)),
                ('address', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=30, serialize=False, primary_key=True, blank=True)),
                ('password', models.CharField(max_length=20)),
                ('contactnumber', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(max_length=500)),
                ('date', models.DateField(max_length=30, null=True, blank=True)),
                ('score', models.IntegerField()),
                ('queno', models.ForeignKey(to='winit.Question')),
                ('username', models.ForeignKey(to='winit.Registration')),
            ],
        ),
        migrations.DeleteModel(
            name='winit',
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(to='winit.Topic'),
        ),
    ]
