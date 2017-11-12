from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Views from apps
# from src.apps.core import views

urlpatterns = [
    # R: indica que a string vai ser uma expressão regular, então caso tenha \n (que no .py significa quebra de linha, vai significar outra coisa, com base no REGEX)
    url(r'^admin/', admin.site.urls),
    # Porque definir um namespace para um include de URL?
    # Caso eu tenha dois namespaces iguais, definirei cada um pelo nome do include antes, exemplo> core:home
    url(r'^', include('src.apps.core.urls', namespace='core')),
    url(r'^curso[s]/', include('src.apps.courses.urls', namespace='courses')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
