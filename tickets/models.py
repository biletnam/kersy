from django.db import models
from plays.models import Showing
# Create your models here.


class Ticket(models.Model):
    showing = models.ForeignKey(Showing)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "{}".format(self.showing.event.name)