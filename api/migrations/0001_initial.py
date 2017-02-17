# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config_key', models.CharField(max_length=40, null=True)),
                ('config_item', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateField(auto_now=True)),
                ('update_time', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Config',
            },
        ),
    ]
