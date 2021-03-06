# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20180520_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='section_portfolio',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='mysite.Section'),
        ),
        migrations.AlterField(
            model_name='page',
            name='section_about_me',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='about_me', to='mysite.Section'),
        ),
    ]
