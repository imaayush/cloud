# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('total_quantity', models.IntegerField()),
                ('total_amount', models.FloatField()),
            ],
        ),
    ]
