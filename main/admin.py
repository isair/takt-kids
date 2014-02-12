from django.contrib import admin
from main.models import *
from main.forms import *
from easy_select2 import select2_modelform


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'start_date', 'end_date')
    ordering = ('-start_date', )


class TicketAdmin(admin.ModelAdmin):
    form = TicketForm
    list_display = ('event', 'ticket_number', 'free', 'voucher_number',
                    'owner_name', 'owner_gender', 'owner_year_of_birth',
                    'notes', 'register_date')
    list_display_links = ('ticket_number', )
    search_fields = ('owner_name', 'ticket_number', 'owner_year_of_birth',
                     'voucher_number', 'owner_name', 'notes')
    list_filter = ('event', 'free', 'owner_gender', 'register_date')
    filter_horizontal = ('achievements', 'cards')
    ordering = ('-register_date', )


class AchievementAdmin(admin.ModelAdmin):
    form = select2_modelform(Achievement)
    list_display = ('event', 'name', 'description')
    list_display_links = ('name', )
    search_fields = ('name', 'description')
    list_filter = ('event', )
    ordering = ('-id', )

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Achievement, AchievementAdmin)
