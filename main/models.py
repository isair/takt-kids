from django.db import models


class Ticket(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    owner_name = models.CharField(max_length=60)
    owner_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ticket_number = models.CharField(max_length=50)
    register_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.owner_name + ' (' + self.ticket_number + ')'

    def clean(self):

        if self.owner_name:
            self.owner_name = ' '.join(self.owner_name.strip().title().split())

        if self.ticket_number:
            self.ticket_number = ' '.join(
                self.ticket_number.strip().upper().split())

        return self
