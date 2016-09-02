from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from category.models import Category
from theaters.models import Venue, Organizer

EVENT_TYPE=(
    ('Premium With Seating', 'Premium With Seating'),
    ('Premium with No Seating', 'Premium with No Seating'),
    ('Free with No Seating', 'Free with No Seating'),
    ('Free with Seating', 'Free with Seating'),
)
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    theater = models.ForeignKey(Venue, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    organizer = models.ForeignKey(Organizer, null=True, blank=True)
    category = models.ManyToManyField(Category)

    type = models.CharField(choices=EVENT_TYPE, null=True, blank=True, max_length=100)
    def __unicode__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"slug": self.slug})

    def get_image_url(self):
        img = self.eventimage_set.first()
        if img:
            return img.image.url
        return img  # None

# TODO(fahad): do something

class Showing(models.Model):
    event = models.ForeignKey(Event)
    date = models.DateField()
    hour = models.CharField(max_length=20, default="First Showing")
    slug = models.SlugField(null=True, blank=True)
    no_of_seats = models.IntegerField(null=True, blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    def __unicode__(self):
        return "{}, {}-{}".format(self.event.title, self.date, self.hour)

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def save(self, *args, **kwargs):
        if not self.id:
            new_slug = "{}-{}".format(self.date, self.event.title)
            self.slug = slugify(new_slug)

        super(Showing, self).save(*args, **kwargs)

    def get_html_price(self):
        if self.sale_price is not None:
            html_text = "<span class='sale-price'>%s</span> <span class='og-price'>%s</span>" % (
                self.sale_price, self.price)
        else:
            html_text = "<span class='price'>%s</span>" % (self.price)
        return mark_safe(html_text)

    def get_absolute_url(self):
        return self.event.get_absolute_url()

    def add_to_cart(self):
        return "%s?item=%s&qty=1" % (reverse("cart"), self.id)

    def remove_from_cart(self):
        return "%s?item=%s&qty=1&delete=True" % (reverse("cart"), self.id)

    def get_title(self):
        return "%s - %s" % (self.event.title, self.date)


def image_upload_to(instance, filename):
    title = instance.event.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "event/%s/%s" % (slug, new_filename)


class EventImage(models.Model):
    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to=image_upload_to)

    def __unicode__(self):
        return self.event.title