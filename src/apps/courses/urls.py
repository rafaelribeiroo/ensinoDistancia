from django.urls import path
from .views import (
    index,
    details,
)

app_name = 'courses'
urlpatterns = [
    path(r'', index, name='index'),
    # Get the parameter of primary key and after, only a digit number
    # path(r'^(?P<pk>\d+)/$', details, name='details'),
    path(r'<str:slug>/', details, name='details'),
]
