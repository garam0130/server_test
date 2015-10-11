from django.shortcuts import render
from mopple.models import *  # noqa


def index(request):
    users = UserInfo.objects.all()
    groups = GroupInfo.objects.all()
    places = Place.objects.all()
    meetings = Meeting.objects.all()
    attendance = Attendance.objects.all()
    args = {'users': users, 'groups': groups, 'places': places, 'meetings': meetings, 'attendances': attendance, }

    return render(request, "index.html", args)
