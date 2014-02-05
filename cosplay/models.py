from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField
from main.models import Ticket


class Cosplayer(models.Model):
    ticket = models.OneToOneField(Ticket)
    picture = ImageField(upload_to='storages.backends.s3boto')
    description = models.CharField(max_length=100)

    def image_thumbnail(self):

        if self.picture:
            return '<img src="%s" width="80" height="80" />' % self.picture.version(ADMIN_THUMBNAIL).url

    image_thumbnail.allow_tags = True
