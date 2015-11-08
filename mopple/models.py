from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Profile(models.Model):
    user = models.OneToOneField(User)
    facebook_id = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.CharField(max_length=20, default='none')
    account_num = models.CharField(default='none', max_length=20)
    account_bank = models.CharField(default='none', max_length=10)
    cookie = models.CharField(default='none', max_length=10)
    sex_list = (
        ('FEMALE', '여자'),
        ('MALE', '남자'),
    )
    sex = models.CharField(max_length=2, choices=sex_list, default='FEMALE')

    def __str__(self):
        return self.user.username


class Academy(models.Model):
    admin_user = models.OneToOneField(User)

    def __str__(self):
        return self.admin_user.username


class Teacher(models.Model):
    user = models.OneToOneField(User)
    academy = models.ForeignKey(Academy)
    contents = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Team(models.Model):
    name = models.CharField(max_length=20)
    balance = models.IntegerField(default=0)
    ass_rate = models.IntegerField(default=0)
    att_rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    cuppon = models.CharField(max_length=50, default='none')
    deposit = models.IntegerField(default=0)
    key = models.CharField(max_length=6, default='none')
    teacher = models.ForeignKey(Teacher, blank=True, null=True)

    def __str__(self):
        return self.name


class Grouping(models.Model):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    balance = models.IntegerField(default=0)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.team.name + '/' + self.user.username


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
    team = models.ForeignKey(Team)
    place = models.ForeignKey(Place, blank=True, null=True)
    homework = models.CharField(max_length=50, default='null')  # to do at that day
    detail = models.TextField(default='none')

    def __str__(self):
        return self.team.name + '/' + str(self.time)


class Penalty(models.Model):
    grouping = models.ForeignKey(Grouping)
    meeting = models.ForeignKey(Meeting)
    time_arrival = models.DateTimeField()
    done_hw = models.BooleanField(default=False)

    def __str__(self):
        return self.grouping.user.__str__() + '/' + self.meeting.__str__()

    def get_att_penalty(self):
        delta = self.meeting.time - self.time_arrival
        if delta >= timedelta(0):
            return 0
        else:
            penalty = abs(delta).seconds/60*self.meeting.team.att_rate
            return round(penalty)

    def get_ass_penalty(self):
        penalty = int(not self.done_hw)*self.meeting.team.ass_rate
        return penalty

    def islate(self):
        return self.get_att_penalty() > 0
