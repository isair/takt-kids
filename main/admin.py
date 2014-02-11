from django.contrib import admin
from main.models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    search_fields = ['name']


class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'owner_name', 'owner_gender',
                    'register_date']
    search_fields = ['owner_name', 'ticket_number']
    filter_horizontal = ('achievements',)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'description')
    search_fields = ('event', 'name', 'description')
    ordering = ('id', )

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Achievement, AchievementAdmin)
