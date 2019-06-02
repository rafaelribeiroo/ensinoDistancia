from django.urls import path
from .views import (
    home,
    contact,
)

app_name = 'core'
urlpatterns = [
    path('', home, name='homepage'),
    path('contato', contact, name='contact'),
]
