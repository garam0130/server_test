from django.shortcuts import render, redirect
from mopple.models import *  # noqa
# from django.contrib.auth.forms import UserCreationForm
from mopple.forms import UserInfoForm
from django.http import HttpResponse
import random
from django.contrib.auth.views import login as auth_login


def index(request):
    users = UserInfo.objects.all()
    groups = GroupInfo.objects.all()
    places = Place.objects.all()
    meetings = Meeting.objects.all()
    # attendance = Attendance.objects.all()
    args = {'users': users, 'groups': groups, 'places': places, 'meetings': meetings, }

    return render(request, "index.html", args)


def signup(request):
    # TODO: no form required. need to parse request.POST
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        # validation check at client side(?)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserInfoForm()
    return render(request, 'form.html', {'form': form, })


def sms_request(request):
    key = random.randrange(1000, 10000)
    return HttpResponse(key)


def login(request):
    auth_login(request, template_name='form.html')
    return auth_login(request, template_name='form.html')
