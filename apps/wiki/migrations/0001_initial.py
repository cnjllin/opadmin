# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 13:32
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='文档标题')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('author', models.CharField(max_length=32, verbose_name='作者')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': 'WiKi文档',
                'verbose_name_plural': 'WiKi文档',
                'db_table': 'wiki',
            },
        ),
    ]
