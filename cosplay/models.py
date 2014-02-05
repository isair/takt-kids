from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from main.models import Ticket


class Cosplayer(models.Model):
    ticket = models.OneToOneField(Ticket)
    picture = ImageField(upload_to='storages.backends.s3boto')
    description = models.CharField(max_length=100)

    def picture_thumbnail(self):

        if self.picture:
            return '<img src="%s" width="80" height="80" />' % get_thumbnail(self.picture, '80x80', quality=99)

    picture_thumbnail.allow_tags = True
