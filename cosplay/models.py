from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail
from main.models import Ticket


class Cosplayer(models.Model):
    ticket = models.OneToOneField(Ticket)
    picture = ImageField(upload_to='storages.backends.s3boto')
    character_name = models.CharField(_('character name'), max_length=100)
    notes = models.CharField(_('notes'), max_length=255, blank=True)
    contest_number = models.IntegerField(blank=True)
    register_date = models.DateTimeField(_('register date'), auto_now_add=True)

    class Meta:
        verbose_name = _('cosplayer')
        verbose_name_plural = _('cosplayers')
        unique_together = (('ticket__event', 'contest_number'), )

    def __unicode__(self):
        return _('Cosplayer %s') % self.ticket.owner_name

    def clean(self):

        if self.character_name:
            self.character_name = ' '.join(
                self.character_name.strip().title().split())

        if self.notes:
            self.notes = ' '.join(
                self.description.strip().lower().split()).capitalize()

    def picture_thumbnail(self):

        if self.picture:
            # return '<img src="%s/%s" width="80" height="80" />' % (settings.MEDIA_URL[:-1],
            # get_thumbnail(self.picture, '80x80', quality=99))
            url = '<img src="//%s.s3.amazonaws.com/media/%s" width="80" />'
            data = (settings.AWS_STORAGE_BUCKET_NAME,
                    get_thumbnail(self.picture, '80x80', quality=99))
            return url % data

    picture_thumbnail.allow_tags = True
