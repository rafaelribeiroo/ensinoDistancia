from django.urls import path
from django.contrib.auth.views import LoginView  # , LogoutView
# from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('entrar/', LoginView.as_view(
        template_name='login.html'), name='login'),
]
