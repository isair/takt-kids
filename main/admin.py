from django.contrib import admin
from main.models import *


class TicketAdmin(admin.ModelAdmin):
    search_fields = ['owner_name', 'ticket_number']

admin.site.register(Ticket, TicketAdmin)
