from django.db import models
from django.contrib.auth.models import User, Group
# from datetime import datetime, timedelta


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    is_male = models.BooleanField(default=True)
    account_number = models.CharField(max_length=20)
    account_bank = models.CharField(max_length=10)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return '[U' + str(self.user.id) + ']' + self.user.username


class GroupInfo(models.Model):
    group = models.OneToOneField(Group)
    deposit = models.CharField(max_length=20)
    att_panelty = models.IntegerField(default=0)
    ass_panelty = models.IntegerField(default=0)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '[G' + str(self.group.id) + ']' + self.group.name


class Place(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    lnglat = models.CharField(max_length=50, blank=True, null=True)

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]

    def __str__(self):
        return self.name


# 1 group N meeting
class Meeting(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    time = models.DateTimeField()
    group = models.ForeignKey(Group)
    place = models.ForeignKey(Place, blank=True, null=True)
    homework = models.CharField(max_length=40, blank=True, null=True)  # to do at that day

    def __str__(self):
        return '[U' + str(self.group.id) + ']' + str(self.time.date())


class Attendance(models.Model):
    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey(User)
    time_arrival = models.DateTimeField()
    done_hw = models.BooleanField(default=False)

    def __str__(self):
        return '[G' + str(self.meeting.group.id) + ']' + self.user.username

    def get_delta(self):
        delta = self.meeting.time - self.time_arrival
        return abs(delta).seconds
