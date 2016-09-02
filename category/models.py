from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from hvad.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    title = models.CharField(max_length=90, unique=True, null=True, blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.slug or u''

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class Meta:
        unique_together = ('slug', 'parent_category',)
        ordering = ["slug"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)