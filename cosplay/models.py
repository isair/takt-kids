from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail
from main.models import Ticket


class Cosplayer(models.Model):
    ticket = models.OneToOneField(Ticket)
    picture = ImageField(upload_to='storages.backends.s3boto')
    description = models.CharField(_('description'), max_length=100)

    class Meta:
        verbose_name = _('cosplayer')
        verbose_name_plural = _('cosplayers')

    def __unicode__(self):
        return _('Cosplayer %s') % self.ticket.owner_name

    def clean(self):

        if self.description:
            self.description = ' '.join(
                self.description.strip().lower().split()).capitalize()

    def picture_thumbnail(self):

        if self.picture:
            # return '<img src="%s/%s" width="80" height="80" />' % (settings.MEDIA_URL[:-1],
            # get_thumbnail(self.picture, '80x80', quality=99))
            return '<img src="//%s.s3.amazonaws.com/media/%s" width="80" height="80" />' % (settings.AWS_STORAGE_BUCKET_NAME,
                                                                   get_thumbnail(self.picture, '80x80', quality=99))

    picture_thumbnail.allow_tags = True
