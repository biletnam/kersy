from django.conf.urls import url, include

from . import views

app_name = 'category'

urlpatterns = [
    url(r'^category/(?P<slug>.+)$', views.CategoryDetail.as_view(), name='detail'),
    url(r'^category/$', views.CategoryList.as_view(), name='list'),
    url(r'^categories/$', views.parent_list, name='parents'),
]