from django.contrib import admin
from main.models import get_current_event
from sorl.thumbnail.admin import AdminImageMixin
from easy_select2 import select2_modelform
from cosplay.models import *

import reversion


class CosplayerAdmin(AdminImageMixin, reversion.VersionAdmin):
    form = select2_modelform(Cosplayer)
    list_display = ('picture_thumbnail', 'character_name',
                    'ticket', 'notes', 'contest_number', 'register_date')
    list_display_links = ('character_name', )
    search_fields = ('character_name', 'ticket', 'notes', 'contest_number')
    list_filter = ('register_date', )
    ordering = ('-register_date', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ticket":
            kwargs["queryset"] = Ticket.objects.filter(event=get_current_event())
        return super(CosplayerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class VoteAdmin(reversion.VersionAdmin):
    form = select2_modelform(Vote)
    list_display = ('voter', 'contestant', 'vote_date')
    list_display_links = ('voter', )
    search_fields = ('voter', 'contestant')
    list_filter = ('vote_date', )
    ordering = ('-vote_date', )


admin.site.register(Cosplayer, CosplayerAdmin)
admin.site.register(Vote, VoteAdmin)
