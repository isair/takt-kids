from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxLengthValidator

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
    character_name = models.CharField(_('character name'), max_length=100)
    COSTUME_CATEGORIES = (
        ('V', 'Video Game Character'),
        ('O', 'Original Character'),
        ('', 'Other')
    )
    costume_category = models.CharField(default='', choices=COSTUME_CATEGORIES, max_length=1, null=True)
    made_own_costume = models.BooleanField(_('made own costume'), default=False)
    email = models.EmailField(_('email'), null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True,
                                    validators=[
                                        RegexValidator(
                                            r'^\+?1?\d{9,15}$',
                                            _('Phone number must be entered in the format: \'+999999999\'. Up to 15 digits allowed.'),
                                            _('Invalid Phone number'),
                                        ),
                                        MaxLengthValidator(15)
                                    ])
    picture = ImageField(upload_to=u_file_rename, blank=True)
    contest_number = models.IntegerField(null=True, blank=True)
    notes = models.CharField(_('notes'), max_length=512, blank=True)
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
    contestant = models.ForeignKey(Cosplayer)
    vote_date = models.DateTimeField(_('vote date'), auto_now_add=True)

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
        unique_together = (('voter', 'contestant'), )

    def __unicode__(self):
        return _('%s\'s vote for %s') % (self.voter, self.contestant)

    def clean(self):
        return


class JuryVote(models.Model):
    jury_member = models.ForeignKey(User)
    contestant = models.ForeignKey(Cosplayer)
    vote_points = models.IntegerField(_('points'))
    vote_date = models.DateTimeField(_('vote date'), auto_now_add=True)

    class Meta:
        verbose_name = _('jury vote')
        verbose_name_plural = _('jury votes')

    def __unicode__(self):
        return _('%s\'s vote for %s') % (self.jury.first_name, self.contestant)

    def clean(self):
        return
