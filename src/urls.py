from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Views from apps
# from src.apps.core import views
from src.apps.core import urls as core_urls
from src.apps.courses import urls as courses_urls
from src.apps.accounts import urls as accounts_urls

app_name = 'src'
urlpatterns = [
    # R: indica que a string vai ser uma expressão regular, então caso tenha \n (que no .py significa quebra de linha, vai significar outra coisa, com base no REGEX)
    path('admin/', admin.site.urls),
    # Porque definir um namespace para um include de URL?
    # Caso eu tenha dois namespaces iguais, definirei cada um pelo nome do include antes, exemplo> core:home
    path('', include(core_urls, namespace='core')),
    path('curso[s]/', include(courses_urls, namespace='courses')),
    path('conta/', include(accounts_urls, namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
