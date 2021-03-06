# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20181029_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='task1_status',
            field=models.CharField(choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], default='To Do', max_length=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='task2_status',
            field=models.CharField(blank=True, choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='task3_status',
            field=models.CharField(blank=True, choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='task4_status',
            field=models.CharField(blank=True, choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=5),
        ),
        migrations.AlterField(
            model_name='project',
            name='task5_status',
            field=models.CharField(blank=True, choices=[('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=5),
        ),
    ]
