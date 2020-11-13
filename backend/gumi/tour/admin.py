from django.contrib import admin
from .models import Place, Mission, CustomMission, Course

admin.site.register(Course)
admin.site.register(Place)
admin.site.register(Mission)
admin.site.register(CustomMission)