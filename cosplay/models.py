from django.db import models
from main.models import Ticket


class Cosplayer(models.Model):
    ticket = models.OneToOneField(Ticket)
    picture = models.ImageField(upload_to='storages.backends.s3boto')
    description = models.CharField(max_length=100)
    pass
