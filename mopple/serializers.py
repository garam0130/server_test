from rest_framework import serializers
from mopple.models import *


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Student
        fields = ('username', 'sex', 'facebook_id', 'account_num', 'account_bank', )


class MeetingSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name')
    place_name = serializers.CharField(source='place.name')
    class Meta:
        model = Meeting
        fields = ('title', 'time', 'team_name', 'place_name', 'homework')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', )


class PenaltySerializer(serializers.ModelSerializer):
    place = serializers.CharField(source='meeting.place')
    team_name = serializers.CharField(source='meeting.team.name')

    class Meta:
        model = Penalty
        fields = ('time_arrival', 'team_name', 'place', 'get_ass_penalty', 'get_att_penalty')
