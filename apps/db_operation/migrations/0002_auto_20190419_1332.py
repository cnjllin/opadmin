# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0002_auto_20190419_1332'),
        ('db_operation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='dblogs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作用户'),
        ),
        migrations.AddField(
            model_name='dbconfig',
            name='server',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Hosts', verbose_name='服务器'),
        ),
        migrations.AlterUniqueTogether(
            name='dbconfig',
            unique_together=set([('server', 'user', 'password')]),
        ),
    ]
