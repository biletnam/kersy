from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category
# Create your views here.

class CategoryList(ListView):
    template_name = 'category/category_list.html'
    model = Category
    context_object_name = 'categories'
    paginate_by = 12


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    slug_url_kwarg = 'slug'

class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# TODO: add parent list view
def parent_list(request):
    parents = Category.objects.filter(parent_category__isnull=False)

    return render(request, 'category/parent_list.html', {'parents': parents})

# TODO: category pagination

def parents(request, hierarchy):
    category_slugs = hierarchy.split('/')
    categories = []
    for slug in category_slugs:
        if not categories:
            parent_category = None
        else:
            parent_category = categories[-1]
        category = get_object_or_404(Category, slug=slug, parent_category=parent_category)
        categories.append(category)
    return render(request, 'category/parent_list.html', {'parents': categories})
