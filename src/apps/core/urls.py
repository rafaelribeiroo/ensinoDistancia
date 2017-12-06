from django.urls import path
from .views import (
    home,
    contact,
)

app_name = 'core'
urlpatterns = [
    path(r'', home, name='homepage'),
    path(r'contato', contact, name='contact'),
]
