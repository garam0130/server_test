# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mopple', '0003_auto_20151011_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('penalty', models.CommaSeparatedIntegerField(max_length=20)),
                ('expense', models.CommaSeparatedIntegerField(max_length=20)),
                ('balance', models.CommaSeparatedIntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('money', models.CommaSeparatedIntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_arrival', models.DateTimeField()),
                ('done_hw', models.BooleanField(default=False)),
                ('grouping', models.ForeignKey(to='mopple.Grouping')),
            ],
        ),
        migrations.CreateModel(
            name='Standard_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('standard_late', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='meeting',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='user',
        ),
        migrations.RemoveField(
            model_name='groupinfo',
            name='deposit',
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='cuppon',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='deposit_amount',
            field=models.CommaSeparatedIntegerField(null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='detail',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='ass_penalty',
            field=models.CommaSeparatedIntegerField(max_length=10, default=0),
        ),
        migrations.AlterField(
            model_name='groupinfo',
            name='att_penalty',
            field=models.CommaSeparatedIntegerField(max_length=10, default=0),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.AddField(
            model_name='grouping',
            name='group',
            field=models.ForeignKey(to='mopple.GroupInfo'),
        ),
        migrations.AddField(
            model_name='grouping',
            name='user',
            field=models.ForeignKey(to='mopple.UserInfo'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='grouping',
            field=models.ForeignKey(to='mopple.Grouping'),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='standard_late',
            field=models.ManyToManyField(to='mopple.Standard_Attendance'),
        ),
    ]
