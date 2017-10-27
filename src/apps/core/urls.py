from django.conf.urls import url, include
from django.contrib import admin

from .views import (
	contact,
	)

urlpatterns = [
	url(r'contato/$', contact, name='contact')
]