from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.db.models import Count
from main.models import *

import reversion


class EventAdmin(reversion.VersionAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'start_date', 'end_date')
    ordering = ('-start_date', )


class TicketAdmin(reversion.VersionAdmin):
    list_display = ('event', 'ticket_number', 'free', 'voucher_number',
                    'owner_name', 'owner_gender', 'owner_year_of_birth',
                    'achievement_count', 'notes', 'register_date')
    list_display_links = ('ticket_number', )
    search_fields = ('owner_name', 'ticket_number', 'owner_year_of_birth',
                     'voucher_number', 'owner_name', 'notes')
    list_filter = ('event', 'free', 'owner_gender', 'register_date')
    filter_horizontal = ('achievements', 'cards')
    ordering = ('-register_date', )

    def get_object(self, request, object_id):
        self.obj = super(TicketAdmin, self).get_object(request, object_id)
        return self.obj

    def queryset(self, request):
        return Ticket.objects.annotate(achievement_count=Count('achievements'))

    def achievement_count(self, obj):
        return obj.achievement_count

    achievement_count.admin_order_field = 'achievement_count'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if (db_field.name == "achievements" or db_field.name == 'cards') and getattr(self, 'obj', None):
            kwargs['queryset'] = Achievement.objects.filter(event=self.obj.event)
        return super(TicketAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


class AchievementAdmin(reversion.VersionAdmin):
    list_display = ('event', 'name', 'description')
    list_display_links = ('name', )
    search_fields = ('name', 'description')
    list_filter = ('event', )
    ordering = ('-id', )


class FreeloaderAdmin(reversion.VersionAdmin):
    list_display = ('event', 'name', 'gender',
                    'year_of_birth', 'notes', 'register_date')
    list_display_links = ('name', )
    search_fields = ('name', 'year_of_birth', 'notes')
    list_filter = ('event', 'gender', 'register_date')
    ordering = ('-register_date', )


class LogAdmin(admin.ModelAdmin):

    list_display = ('action_time', 'user', 'content_type',
                    'change_message', 'is_addition', 'is_change',
                    'is_deletion')
    list_filter = ['action_time', 'user', 'content_type']
    ordering = ('-action_time',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Freeloader, FreeloaderAdmin)
admin.site.register(LogEntry, LogAdmin)
