from django.conf.urls import url
from . import views as plays_views

app_name = 'events'


urlpatterns = [
    url(r'^$', plays_views.PlayList.as_view(), name="event_list"),
    url(r'^(?P<slug>[\w.@+-]+)/$', plays_views.PlayDetail.as_view(), name='event_detail'),

    url(r'^showings/$', plays_views.ShowingList.as_view(), name='showing_list'),
    url(r'^showings/(?P<slug>[\w.@+-]+)/$', plays_views.ShowingDetail.as_view(), name='showing_detail'),

]