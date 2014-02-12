from django import forms
from easy_select2 import select2_meta_factory
from main.models import Ticket


class TicketForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)
    Meta = select2_meta_factory(Ticket)
