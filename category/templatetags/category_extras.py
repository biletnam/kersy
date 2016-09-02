from django import template

from category.models import Category

register = template.Library()


@register.inclusion_tag('templatetags/category_nav.html')
def nav_category_list():
    categories = Category.objects.all()
    return {'categories': categories}

@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)