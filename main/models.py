from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Event(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __unicode__(self):
        return self.name

    def clean(self):

        # Format name (e.g.: Kontakt Live 2400)
        if self.name:
            self.name = ' '.join(self.name.strip().title().split())


class Ticket(models.Model):
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other'))
    )
    event = models.ForeignKey('Event')
    owner_name = models.CharField(_('owner name'), max_length=60)
    owner_gender = models.CharField(
        _('owner gender'), max_length=1, choices=GENDER_CHOICES)
    owner_year_of_birth = models.PositiveIntegerField(_('year of birth'))
    ticket_number = models.PositiveIntegerField(_('ticket number'))
    free = models.BooleanField(_('free'))
    voucher_number = models.IntegerField(
        _('voucher number'), null=True, blank=True)
    notes = models.CharField(_('notes'), max_length=255, blank=True)
    register_date = models.DateTimeField(_('register date'), auto_now_add=True)
    achievements = models.ManyToManyField(
        'Achievement', verbose_name=_('achievements'), blank=True)
    cards = models.ManyToManyField(
        'Achievement', verbose_name=_('cards'), related_name=_('cards'),
        blank=True)

    class Meta:
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')
        unique_together = (('event', 'ticket_number'), )

    def __unicode__(self):
        return '{0} ({1})'.format(self.owner_name, self.ticket_number)

    def clean(self):

        # Format name (e.g.: John Janette Johnson)
        if self.owner_name:
            self.owner_name = ' '.join(self.owner_name.strip().title().split())

        if self.voucher_number is not None:

            # If there is a voucher number, make sure this is a free ticket
            self.free = True

            # Unique pair enforcement: ('event', 'voucher_number')
            queryset = Ticket.objects.exclude(
                id=self.id).filter(
                voucher_number=self.voucher_number).filter(
                event=self.event)
            if queryset.exists():
                raise ValidationError(
                    _('This voucher name is already used at this event.'))


class Achievement(models.Model):
    event = models.ForeignKey('Event')
    name = models.CharField(_('name'), max_length=80)
    description = models.CharField(
        _('description'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('achievement')
        verbose_name_plural = _('achievements')

    def __unicode__(self):
        return self.name

    def clean(self):

        # Format name (e.g.: Walked 100 Miles)
        if self.name:
            self.name = ' '.join(self.name.strip().title().split())

        # Format description (e.g.: Given to people who walk 100 miles)
        if self.description:
            self.description = ' '.join(
                self.description.strip().lower().split()).capitalize()


class Freeloader(models.Model):
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other'))
    )
    event = models.ForeignKey('Event')
    name = models.CharField(_('name'), max_length=60)
    gender = models.CharField(
        _('gender'), max_length=1, choices=GENDER_CHOICES)
    year_of_birth = models.PositiveIntegerField(_('year of birth'))
    notes = models.CharField(_('notes'), max_length=255, blank=True)
    register_date = models.DateTimeField(_('register date'), auto_now_add=True)

    class Meta:
        verbose_name = _('freeloader')
        verbose_name_plural = _('freeloaders')

    def __unicode__(self):
        return self.name

    def clean(self):

        # Format name (e.g.: Cristopher Walken)
        if self.name:
            self.name = ' '.join(self.name.strip().title().split())

        # Format notes (e.g.: Free entrance for awesomeness)
        if self.notes:
            self.notes = ' '.join(
                self.notes.strip().lower().split()).capitalize()
