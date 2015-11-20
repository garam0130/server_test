from django.shortcuts import render
from mopple.models import *
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.models import User
from mopple.serializers import StudentSerializer
from mopple.serializers import UserSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def index(request):
    return render(request, "index.html")


def login(request):
    auth_login(request, template_name='form.html')
    return auth_login(request, template_name='form.html')
