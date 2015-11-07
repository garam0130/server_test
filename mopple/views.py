from django.shortcuts import render, redirect
from mopple.models import *  # noqa
# from django.contrib.auth.forms import UserCreationForm
from mopple.forms import ProfileForm
from django.http import HttpResponse
import random
from django.contrib.auth.views import login as auth_login


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            facebook_id = form.cleaned_data.get('facebook_id')
            profile = Profile(user=user, facebook_id=facebook_id)
            profile.save()
            return redirect('index')
    else:
        form = ProfileForm()
    return render(request, 'form.html', {'form': form, })


def sms_request(request):
    key = random.randrange(1000, 10000)
    return HttpResponse(key)


def login(request):
    auth_login(request, template_name='form.html')
    return auth_login(request, template_name='form.html')
