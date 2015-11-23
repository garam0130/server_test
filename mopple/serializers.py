from rest_framework import serializers
from mopple.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    penalty = serializers.PrimaryKeyRelatedField(many=True, queryset=Penalty.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    academy = serializers.PrimaryKeyRelatedField(queryset=Academy.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'penalty', 'student', 'teacher', 'academy')

        

class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PenaltySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Penalty
        fields = '__all__'
