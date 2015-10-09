# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_arrival', models.DateTimeField()),
                ('done_hw', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('deposit', models.CharField(max_length=20)),
                ('att_panelty', models.IntegerField(default=0)),
                ('ass_panelty', models.IntegerField(default=0)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField(null=True, blank=True)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=20, null=True, blank=True)),
                ('time', models.DateTimeField()),
                ('homework', models.CharField(max_length=40, null=True, blank=True)),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('lnglat', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_male', models.BooleanField(default=True)),
                ('account_number', models.CharField(max_length=20)),
                ('account_bank', models.CharField(max_length=10)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='place',
            field=models.ForeignKey(null=True, to='mopple.Place', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='meeting',
            field=models.ForeignKey(to='mopple.Meeting'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
