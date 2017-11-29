from django.conf.urls import url  # include
from django.contrib.auth import views


urlpatterns = [
    url(r'^entrar/$', views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
]