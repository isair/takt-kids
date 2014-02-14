from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from easy_select2 import select2_modelform
from cosplay.models import *


class CosplayerAdmin(AdminImageMixin, admin.ModelAdmin):
    form = select2_modelform(Cosplayer)
    list_display = ('event', 'picture_thumbnail', 'character_name',
                    'ticket', 'notes', 'contest_number', 'register_date')
    list_display_links = ('character_name', )
    search_fields = ('character_name', 'ticket', 'notes', 'contest_number')
    list_filter = ('event', 'register_date')
    ordering = ('-register_date', )


class VoteAdmin(admin.ModelAdmin):
    form = select2_modelform(Vote)
    list_display = ('event', 'voter', 'contestant', 'vote_date')
    list_display_links = ('voter', )
    search_fields = ('voter', 'contestant')
    list_filter = ('event', 'vote_date')
    ordering = ('-vote_date', )


admin.site.register(Cosplayer, CosplayerAdmin)
admin.site.register(Vote, VoteAdmin)
