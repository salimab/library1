from django.conf.urls import url

from personal.models import Book
from . import views
from django.contrib.auth.views import login
from django.views.generic import ListView, DetailView


urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^login/$', login, {'template_name': 'personal/login.html'}),
    url(r'^lib/$', ListView.as_view(queryset=Book.objects.all().order_by("-date")[:25],
                                template_name = "personal/lib.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Book,
                                            template_name='personal/book.html'))
]

