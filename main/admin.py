from django.contrib import admin
from main.models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'owner_name', 'owner_gender',
                    'register_date']
    search_fields = ['owner_name', 'ticket_number']

admin.site.register(Event)
admin.site.register(Ticket, TicketAdmin)
