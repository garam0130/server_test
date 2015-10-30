from django.contrib import admin
from mopple.models import *  # noqa

admin.site.register(UserInfo)
admin.site.register(GroupInfo)
admin.site.register(Meeting)
admin.site.register(Place)
admin.site.register(Penalty)
admin.site.register(Grouping)
