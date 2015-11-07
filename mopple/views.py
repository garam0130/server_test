from django.shortcuts import render, redirect
from mopple.models import *  # noqa
from mopple.forms import ProfileForm
from django.http import HttpResponse
import random
from django.contrib.auth.views import login as auth_login
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, "index.html")

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if request.method == 'POST':    
            print(repr(request.body.decode('utf8')))
            data=json.loads(request.body.decode('utf-8'))
            a = data['facebookid']
            b = data['username']
            c = data['password']
            print('a의 값은')
            print(a)
            print('b의 값은')
            print(b)
            print('c의 값은')
            print(c)
            return HttpResponse('post요청입니다')
    else:
        return HttpResponse('get요청입니다')
    

def sms_request(request):
    key = random.randrange(1000, 10000)
    return HttpResponse(key)


def login(request):
    auth_login(request, template_name='form.html')
    return auth_login(request, template_name='form.html')
