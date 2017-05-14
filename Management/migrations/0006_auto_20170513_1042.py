# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_auto_20170513_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default='\u4e0a\u6d77\u5e02\u5609\u5b9a\u533a\u66f9\u5b89\u516c\u8def4800\u53f7', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='average',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='grade',
            name='lesson1',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='grade',
            name='lesson2',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='grade',
            name='lesson3',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='average',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='level1',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='level2',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='level3',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='level4',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='level5',
            field=models.DecimalField(decimal_places=2, default=60.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.DecimalField(decimal_places=0, default=25, max_digits=3),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(default='F', max_length=1),
        ),
    ]