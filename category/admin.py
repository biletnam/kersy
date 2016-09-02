from django.contrib import admin
import csv

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse
from hvad.admin import TranslatableAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'parent_category']
    list_editable = ['parent_category']
    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('title')


admin.site.register(Category, CategoryAdmin)