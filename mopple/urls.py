from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from mopple.views import PostViewSet, UserViewSet
from rest_framework import renderers
from mopple import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'user', views.UserViewSet)


post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meeting/$', views.MeetingList.as_view()),
    url(r'^meeting/(?P<pk>[0-9]+)/$', views.MeetingDetail().as_view()),
    url(r'^team/$', views.TeamList().as_view()),
    url(r'^team/(?P<pk>[0-9]+)/$', views.TeamDetail().as_view()),
    url(r'^student/$', views.StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
]

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]