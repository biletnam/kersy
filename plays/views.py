from django.shortcuts import render
from django.views import generic

from category.models import Category
from .models import Event, Showing


# Create your views here.

class PlayList(generic.ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

class ShowingList(generic.ListView):
    model = Showing
    template_name = 'events/showing_list.html'

    context_object_name = 'shows'

class PlayDetail(generic.DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'

class ShowingDetail(generic.DetailView):
    model = Showing
    template_name = 'events/showing_detail.html'
    context_object_name = 'showing'


def home(request):
    title = 'Sign Up Now'

    events = Event.objects.all().order_by("?")[:6]
    categories = Category.objects.all()
    context = {
        "title": title,
        "events": events,
        "categories": categories,
    }


    return render(request, "home.html", context)
