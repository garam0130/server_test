from django.conf.urls import include, url
from django.contrib import admin
from mopple.views import *
from mopple import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'meeting', views.MeetingViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'penalty', views.PenaltyViewSet)
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

meeting_list = MeetingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
meeting_detail = MeetingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
penalty_list = PenaltyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
penalty_detail = PenaltyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
team_list = TeamViewSet.as_view({
    'get': 'list'
})
team_detail = TeamViewSet.as_view({
    'get': 'retrieve'
})
student_list = StudentViewSet.as_view({
    'get': 'list'
})
student_detail = StudentViewSet.as_view({
    'get': 'retrieve'
})

