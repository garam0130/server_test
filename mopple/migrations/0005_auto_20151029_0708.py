# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mopple', '0004_auto_20151015_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='cuppon',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='deposit_amount',
            field=models.CommaSeparatedIntegerField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='money',
            field=models.CommaSeparatedIntegerField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='detail',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(default='noname', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='account_bank',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='account_number',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
