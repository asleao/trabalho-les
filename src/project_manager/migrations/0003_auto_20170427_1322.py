# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_manager', '0002_auto_20170427_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dono', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='participantes',
        ),
        migrations.AddField(
            model_name='projeto',
            name='participantes',
            field=models.ManyToManyField(related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
