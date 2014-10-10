from django import forms
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

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(CosplayerAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'notes':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


# TODO: Currently a voter can only give a single vote.
# Ideally, we want voters to be able to give one vote for each gender.
class VoteAdmin(reversion.VersionAdmin):
    form = select2_modelform(Vote)
    list_display = ('voter', 'contestant', 'vote_date')
    list_display_links = ('voter', )
    search_fields = ('voter', 'contestant')
    list_filter = ('vote_date', )
    ordering = ('-vote_date', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'voter':
            kwargs['queryset'] = Ticket.objects.filter(event=get_current_event())
        elif db_field.name == 'contestant':
            kwargs['queryset'] = Cosplayer.objects.filter(ticket__event=get_current_event())
        return super(VoteAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class JuryVoteAdmin(reversion.VersionAdmin):
    form = select2_modelform(JuryVote)
    list_display = ('jury_member', 'contestant', 'vote_points', 'vote_date')
    list_display_links = ('jury_member', )
    search_fields = ('jury_member', 'contestant')
    list_filter = ('vote_points', 'vote_date')
    ordering = ('-vote_date', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'contestant':
            kwargs['queryset'] = Cosplayer.objects.filter(ticket__event=get_current_event())
        return super(JuryVoteAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.jury_member = request.user
        obj.save()


admin.site.register(Cosplayer, CosplayerAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(JuryVote, JuryVoteAdmin)
