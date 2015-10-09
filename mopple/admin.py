from django.contrib import admin
from mopple.models import UserInfo, GroupInfo, Meeting, Place, Attendance

admin.site.register(UserInfo)
admin.site.register(GroupInfo)
admin.site.register(Meeting)
admin.site.register(Place)
admin.site.register(Attendance)
