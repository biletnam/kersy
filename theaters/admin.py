from django.contrib import admin

# Register your models here.
from .models import Venue, Organizer

admin.site.register(Venue)
admin.site.register(Organizer)