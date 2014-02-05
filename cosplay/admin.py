from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from cosplay.models import *


class CosplayerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['picture', 'description']
    search_fields = ['description']
    pass

admin.site.register(Cosplayer, CosplayerAdmin)
