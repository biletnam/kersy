from django.contrib import admin
from .models import Event, Showing, EventImage
# Register your models here.

class ImageInline(admin.TabularInline):
    model = EventImage

class EventAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

    list_display = ['title', 'start_date', 'end_date']

admin.site.register(Event, EventAdmin)
admin.site.register(Showing)
admin.site.register(EventImage)
