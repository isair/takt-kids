from django.db import models


class Attendant(models.Model):
    name = models.CharField(max_length=60)
    is_male = models.BooleanField()


class Ticket(models.Model):
    uid = models.CharField(max_length=50)
