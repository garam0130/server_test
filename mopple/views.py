from django.shortcuts import render, redirect
from mopple.models import *
from django.http import HttpResponse
import random
from django.contrib.auth.views import login as auth_login
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data=json.loads(request.body.decode('utf-8'))
        a = User.objects.create_user(username=data['username'], password=data['password'])
        a.save()
        b = Profile.objects.create(user=a, facebook_id=data['facebookid'])
        b.save()
        msg1 = '회원가입 원료' + '\n' + '유저아이디는 ' + a.username + '\n' + '유저 패스워드는 ' + a.password
        msg2 = 'profile 등록 완료.' + '\n' + a.username + '님의 페이스북 아이디는 ' + str(b.facebook_id)
        return_msg = msg1 + '\n' + msg2
        return HttpResponse(return_msg)
    else:
        return HttpResponse('get 요청입니다')


def sms_request(request):
    key = random.randrange(1000, 10000)
    return HttpResponse(key)


def login(request):
    auth_login(request, template_name='form.html')
    return auth_login(request, template_name='form.html')
