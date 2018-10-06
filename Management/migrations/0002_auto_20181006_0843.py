# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-06 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessontwo',
            name='level4',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='lessontwo',
            name='level5',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default='avatar/timg.jpg', upload_to='avatar'),
        ),
    ]
