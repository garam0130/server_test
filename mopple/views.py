from mopple.models import Student, Meeting, Team, Penalty
from django.contrib.auth.models import User
from mopple.serializers import StudentSerializer, UserSerializer, TeamSerializer, MeetingSerializer, PenaltySerializer
from rest_framework import permissions
from mopple.permissions import IsOwner
from rest_framework import viewsets


class PenaltyViewSet(viewsets.ModelViewSet):
    queryset = Penalty.objects.all()
    serializer_class = PenaltySerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return self.request.user.penalty

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAdminUser,)

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsOwner,)
