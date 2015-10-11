# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mopple', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupinfo',
            old_name='ass_panelty',
            new_name='ass_penalty',
        ),
        migrations.RenameField(
            model_name='groupinfo',
            old_name='att_panelty',
            new_name='att_penalty',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(to='mopple.UserInfo'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='group',
            field=models.ForeignKey(to='mopple.GroupInfo'),
        ),
    ]
