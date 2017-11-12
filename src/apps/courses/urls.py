from django.conf.urls import url
from .views import (
    index,
    details,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    # Get the parameter of primary key and after, only a digit number
    # url(r'^(?P<pk>\d+)/$', details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),
]
