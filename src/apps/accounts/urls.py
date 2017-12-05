from django.conf.urls import url  # include
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^entrar/$', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
]
