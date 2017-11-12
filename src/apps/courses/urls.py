from django.conf.urls import url
from .views import (
    index,
    details,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<pk>\d+)/$', details, name='details'),
]
