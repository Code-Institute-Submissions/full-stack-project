# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181120_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='staticfiles/profile_img/anon.png', upload_to='profile_img'),
        ),
    ]
