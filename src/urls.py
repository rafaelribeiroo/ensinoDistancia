"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

#Views from apps
#from src.apps.core import views

urlpatterns = [
	#R: indica que a string vai ser uma expressão regular, então caso tenha \n (que no .py significa quebra de linha, vai significar outra coisa, com base no REGEX)
    url(r'^admin/', admin.site.urls),
    url(r'^', include('src.apps.core.urls'))
]
