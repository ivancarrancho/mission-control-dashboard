# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalyticsSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('ga_view_id', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAnalyticsSiteGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('ga_metric_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
    ]
