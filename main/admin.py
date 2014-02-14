from django.contrib import admin
from main.models import *
from main.forms import *


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
    list_display = ('event', 'name', 'description')
    list_display_links = ('name', )
    search_fields = ('name', 'description')
    list_filter = ('event', )
    ordering = ('-id', )


class FreeloaderAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'gender',
                    'year_of_birth', 'notes', 'register_date')
    list_display_links = ('name', )
    search_fields = ('name', 'year_of_birth', 'notes')
    list_filter = ('event', 'gender', 'register_date')
    ordering = ('-register_date', )

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Freeloader, FreeloaderAdmin)
