from django.db import models
from django.contrib.auth.models import User, Group
from datetime import timedelta


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    is_male = models.BooleanField(default=True)
    account_number = models.CharField(default='none', max_length=20)
    account_bank = models.CharField(default='none', max_length=10)
    balance = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20, default='none')

    def __str__(self):
        return self.user.username

    def get_cum_panelty(self):
        pass


class Standard_Attendance(models.Model):
    standard_late = models.IntegerField()

    def __str__(self):
        return self.standard_late
        # self.group.id != self.id


class GroupInfo(models.Model):
    group = models.OneToOneField(Group)
    deposit_amount = models.CommaSeparatedIntegerField(max_length=20, default=0)
    ass_penalty = models.CommaSeparatedIntegerField(max_length=10, default=0)  # done or undone
    att_penalty = models.CommaSeparatedIntegerField(max_length=10, default=0)  # 10분당 설정할 수 있게 / 30분 이상시 고정비
    standard_late = models.ManyToManyField(Standard_Attendance)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(blank=True, null=True)
    cuppon = models.CharField(max_length=20, default='none')

    def __str__(self):
        return self.group.name
        # self.group.id != self.id

    def set_ass_penalty(self, time, standard_late):  # standard_late : 이 부분 dictionary 처리 해줘야하는데 잘 모르겠슴.
        if time <= 0:
            self.att_penalty = 0


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
    title = models.CharField(max_length=20, default='noname')
    time = models.DateTimeField()
    group = models.ForeignKey(GroupInfo)  # group.id != groupinfo.id
    place = models.ForeignKey(Place, blank=True, null=True)
    homework = models.CharField(max_length=40, default='null')  # to do at that day
    detail = models.TextField(default='none')

    def __str__(self):
        return str(self.time)


# 개인 유저와 그룹을 이어주는 테이블. 둘다 1:n 관계
class Grouping(models.Model):
    group = models.ForeignKey(GroupInfo)  # group.id != groupinfo.id
    user = models.ForeignKey(UserInfo)  # user.id != userinfo.id
    money = models.CommaSeparatedIntegerField(max_length=20, default='0')

    def __str__(self):
        return self.group.group.name + '/' + self.user.user.username


class Deposit(models.Model):
    grouping = models.ForeignKey(Grouping)
    penalty = models.CommaSeparatedIntegerField(max_length=20)
    expense = models.CommaSeparatedIntegerField(max_length=20)
    balance = models.CommaSeparatedIntegerField(max_length=20)

    def get_balance(self, penalty, expense, balance):
        balance == self.grouping.money - penalty - expense


class Penalty(models.Model):
    grouping = models.ForeignKey(Grouping)
    time_arrival = models.DateTimeField()
    done_hw = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_att_penalty(self):
        delta = self.meeting.time - self.time_arrival
        if delta <= timedelta(0):
            return 0
        else:
            penalty = abs(delta).seconds/60*self.meeting.group.att_penalty
            return penalty

    def get_ass_penalty(self):
        penalty = int(self.done_hw)*self.meeting.group.ass_penalty
        return penalty

    def islate(self):
        return self.get_att_penalty() > 0
