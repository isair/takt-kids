from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from cosplay.models import *


class CosplayerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['picture_thumbnail', 'description', 'ticket']
    search_fields = ['description', 'ticket']

admin.site.register(Cosplayer, CosplayerAdmin)
