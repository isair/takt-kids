from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail
from main.models import Ticket

import uuid


def u_file_rename(instance, filename):
        print filename
        name = uuid.uuid1()
        ext = filename.split('.')[-1]
        return 'cosplayers/%s.%s' % (name, ext)


class Cosplayer(models.Model):
    ticket = models.OneToOneField(Ticket)
    picture = ImageField(upload_to=u_file_rename)
    character_name = models.CharField(_('character name'), max_length=100)
    notes = models.CharField(_('notes'), max_length=255, blank=True)
    contest_number = models.IntegerField(null=True, blank=True)
    register_date = models.DateTimeField(_('register date'), auto_now_add=True)

    class Meta:
        verbose_name = _('cosplayer')
        verbose_name_plural = _('cosplayers')

    def __unicode__(self):
        return _('Cosplayer %s') % self.ticket.owner_name

    def clean(self):

        if self.character_name:
            self.character_name = ' '.join(
                self.character_name.strip().title().split())

        if self.notes:
            self.notes = ' '.join(
                self.notes.strip().lower().split()).capitalize()

    def picture_thumbnail(self):

        if self.picture:
            return '<img src="%s/%s" width="80" height="80" />' % (settings.MEDIA_URL[:-1],
                                                                   get_thumbnail(self.picture, '80x80', quality=99))

    picture_thumbnail.allow_tags = True


class Vote(models.Model):
    voter = models.ForeignKey(Ticket)
    votee = models.ForeignKey(Cosplayer)

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')

    def __unicode__(self):
        return _('%s\'s vote for %s') % (self.voter, self.votee)

    def clean(self):
        return
