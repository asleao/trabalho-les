# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0002_ferramenta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='user',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
