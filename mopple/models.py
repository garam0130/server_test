from django.db import models
from django.contrib.auth.models import User, Group
from datetime import timedelta


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    is_male = models.BooleanField(default=True)
    phone_num = models.CharField(max_length=20, default='none')
    created_at = models.DateTimeField(auto_now_add=True)
    account_num = models.CharField(default='none', max_length=20)
    account_bank = models.CharField(default='none', max_length=10)

    def __str__(self):
        return self.user.username


class GroupInfo(models.Model):
    group = models.OneToOneField(Group)
    balance = models.IntegerField(default=0)
    ass_rate = models.IntegerField(default=0)
    att_rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    cuppon = models.CharField(max_length=50, default='none')

    def __str__(self):
        return self.group.name
        # self.group.id != self.id


class Grouping(models.Model):
    group = models.ForeignKey(GroupInfo)  # group.id != groupinfo.id
    user = models.ForeignKey(UserInfo)  # user.id != userinfo.id
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.group.group.name + '/' + self.user.user.username


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


class Meeting(models.Model):
    title = models.CharField(max_length=20, default='noname')
    time = models.DateTimeField()
    group = models.ForeignKey(GroupInfo)  # group.id != groupinfo.id
    place = models.ForeignKey(Place, blank=True, null=True)
    homework = models.CharField(max_length=50, default='null')  # to do at that day
    detail = models.TextField(default='none')

    def __str__(self):
        return self.group.group.name + '/' + str(self.time)


class Penalty(models.Model):
    grouping = models.ForeignKey(Grouping)
    meeting = models.ForeignKey(Meeting)
    time_arrival = models.DateTimeField()
    done_hw = models.BooleanField(default=False)

    def __str__(self):
        return self.grouping.__str__() + '/' + self.meeting.__str__()

    def get_att_penalty(self):
        delta = self.meeting.time - self.time_arrival
        if delta >= timedelta(0):
            return 0
        else:
            penalty = abs(delta).seconds/60*self.meeting.group.att_penalty
            return round(penalty)

    def get_ass_penalty(self):
        penalty = int(not self.done_hw)*self.meeting.group.ass_penalty
        return penalty

    def islate(self):
        return self.get_att_penalty() > 0
