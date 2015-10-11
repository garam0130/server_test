# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mopple', '0002_auto_20151011_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='homework',
            field=models.CharField(max_length=40, default='null'),
        ),
    ]
