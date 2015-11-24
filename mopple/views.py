from mopple.models import Student, Meeting, Team, Penalty
from mopple.serializers import StudentSerializer, TeamSerializer, MeetingSerializer, PenaltySerializer
from rest_framework import permissions
from rest_framework import viewsets


class PenaltyViewSet(viewsets.ModelViewSet):
    queryset = Penalty.objects
    serializer_class = PenaltySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Penalty.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        meeting_set = []
        for item in user.grouping_set.all():
            for item2 in item.team.meeting_set.all():
                meeting_set.append(item2)
        return meeting_set

    '''#에러가 안난다
    try:
        return user.grouping_set.last().team.meeting_set.all()
    except:
        return None
    '''



class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        team_set = []
        for item in user.grouping_set.all():
            team_set.append(item.team)
        return team_set


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)