from django.conf.urls import url, include
from django.contrib import admin

from .views import (
	home,
	contact,
	)

urlpatterns = [
	url(r'$', home, name='homepage'),
	url(r'^contato[s/]$', contact, name='contact')
]