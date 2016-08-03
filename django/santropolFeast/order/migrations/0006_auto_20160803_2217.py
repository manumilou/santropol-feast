# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_fix241b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('O', 'Ordered'), ('D', 'Delivered'), ('N', 'No Charge'), ('B', 'Billed'), ('P', 'Paid')], max_length=1, verbose_name='order status'),
        ),
    ]
