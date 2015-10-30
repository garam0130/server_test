# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('balance', models.IntegerField(default=0)),
                ('ass_rate', models.IntegerField(default=0)),
                ('att_rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cuppon', models.CharField(max_length=50, default='none')),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('balance', models.IntegerField(default=0)),
                ('group', models.ForeignKey(to='mopple.GroupInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=20, default='noname')),
                ('time', models.DateTimeField()),
                ('homework', models.CharField(max_length=50, default='null')),
                ('detail', models.TextField(default='none')),
                ('group', models.ForeignKey(to='mopple.GroupInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time_arrival', models.DateTimeField()),
                ('done_hw', models.BooleanField(default=False)),
                ('grouping', models.ForeignKey(to='mopple.Grouping')),
                ('meeting', models.ForeignKey(to='mopple.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('lnglat', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_male', models.BooleanField(default=True)),
                ('phone_num', models.CharField(max_length=20, default='none')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account_num', models.CharField(max_length=20, default='none')),
                ('account_bank', models.CharField(max_length=10, default='none')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='place',
            field=models.ForeignKey(to='mopple.Place', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='grouping',
            name='user',
            field=models.ForeignKey(to='mopple.UserInfo'),
        ),
    ]
