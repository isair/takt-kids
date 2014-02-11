from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


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

        if self.name:
            self.name = ' '.join(self.name.strip().title().split())


class Ticket(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    event = models.ForeignKey('Event')
    owner_name = models.CharField(_('owner name'), max_length=60)
    owner_gender = models.CharField(
        _('owner gender'), max_length=1, choices=GENDER_CHOICES)
    ticket_number = models.CharField(_('ticket number'), max_length=50)
    register_date = models.DateTimeField(_('register date'), auto_now_add=True)
    achievements = models.ManyToManyField(
        'Achievement', verbose_name=_('achievements'), blank=True)

    class Meta:
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')
        unique_together = (('event', 'ticket_number'), )

    def __unicode__(self):
        return self.owner_name + ' (' + self.ticket_number + ')'

    def clean(self):

        if self.owner_name:
            self.owner_name = ' '.join(self.owner_name.strip().title().split())

        if self.ticket_number:
            self.ticket_number = ' '.join(
                self.ticket_number.strip().upper().split())

        return self


class Achievement(models.Model):
    event = models.ForeignKey('Event')
    name = models.CharField(_('name'), max_length=30)
    description = models.CharField(
        _('description'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('achievement')
        verbose_name_plural = _('achievements')

    def __unicode__(self):
        return self.name

    def clean(self):

        if self.name:
            self.name = ' '.join(self.name.strip().title().split())

        if self.description:
            self.description = ' '.join(
                self.description.strip().lower().split()).capitalize()
