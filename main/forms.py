from django import forms


class TicketForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)
