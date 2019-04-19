# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
        ('ansible_task', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playbooks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='添加人'),
        ),
        migrations.AddField(
            model_name='playbooklogs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='hosts',
            field=models.ManyToManyField(to='asset.Hosts', verbose_name='主机'),
        ),
        migrations.AddField(
            model_name='ansiblerole',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='添加人员'),
        ),
        migrations.AddField(
            model_name='ansibleoperlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作者'),
        ),
    ]