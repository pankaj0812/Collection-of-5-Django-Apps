# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-08 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_items',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False, verbose_name='checked out'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='create date'),
        ),
    ]
