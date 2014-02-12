from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from easy_select2 import select2_modelform
from cosplay.models import *


class CosplayerAdmin(AdminImageMixin, admin.ModelAdmin):
    form = select2_modelform(Cosplayer)
    list_display = ('picture_thumbnail', 'character_name',
                    'ticket', 'notes', 'contest_number', 'register_date')
    list_display_links = ('character_name', )
    search_fields = ('character_name', 'ticket',
                     'notes', 'contest_number', 'register_date')
    ordering = ('-register_date', )

admin.site.register(Cosplayer, CosplayerAdmin)
