from django.contrib import admin
from .models import Place, Mission, CustomMission

admin.site.register(Place)
admin.site.register(Mission)
admin.site.register(CustomMission)