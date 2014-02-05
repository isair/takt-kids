from django.contrib import admin
from cosplay.models import *


class CosplayerAdmin(admin.ModelAdmin):
    list_display = ['picture', 'description']
    search_fields = ['description']
    pass

admin.site.register(Cosplayer, CosplayerAdmin)
