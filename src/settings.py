#Dica: Defina todas as constantes aqui no settings, que depois você pode usá-las de uma forma mais enxuta

#Pacote que basicamente lida com os diretórios em nossa máquina e faz o python interagir com eles
import os
from decouple import config

# Onde será a base do nosso diretório? Será o meu 'src' (forma como gosto de renomear, geralmente é o nome que apelido no django-admin startproject src .)
# print(BASE_DIR) <- Isso irá mostrar o caminho quando eu: $ python manage.py runserver
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Uma medida de segurança para a autenticação nativa do Django (Na hora de trocar a senha), é criptografado.
SECRET_KEY = config('SECRET_KEY')

# Uma ferramenta de debug nativa do Django (Como o interpretador PY) que informa as possíveis exceções (erros) quando está desenvolvendo, ao setar False ele dará as famosas mensagens de erro que o usuário conhece (404, 500), quando desativa é requerido informar os HOSTS que poderão acessar a app. Ex: '*' (for all), '*.interfaceJuridica.com' (que poderá ser www. ou sem o www), outra medida de segurança para garantir que ninguém 'roube' seu site
# Aviso Importante: Nunca deixe Debug ativado em produção
DEBUG = config('DEBUG', default=True, cast=bool)

# Diretiva: Isso define uma lista de nomes e domínios que podem ser usados para ser conectados em instância do Django, o Django requer que você defina isso para evitar uma vulnerabilidade de segurança.
ALLOWED_HOSTS = []

# São as apps nativas do Django, você pode utilizá-las ou não
INSTALLED_APPS = [
    # My App Principal
    'src.apps.core',

    # Django Apps
    'django.contrib.admin', # CMS do Django
    'django.contrib.auth', # Autenticação
    'django.contrib.contenttypes', # Tipos de conteúdo (Chave estrangeira genérica)
    'django.contrib.sessions', # Sessões (Cookies)
    'django.contrib.messages', # Mensagens
    'django.contrib.staticfiles', # Arquivos estáticos

    # My Apps
    'src.apps.courses',
    'src.apps.accounts',
]

# Pacotes de software que permitem que você mude o jeito que as aplicações do Django interagem com o servidor entre requisições e respostas
# Requisição: Quando um usuário visita nossa homepage
# Resposta:   A requisição chega ao servidor e o mesmo retorna uma página que o usuário solicitou
# O middleware nos permite interagir com o procedimento do conjunto
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Rota para nosso arquivo de rotas URL, que manipulam nossos 'hosts' para deixarem mais amigáveis
ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django possui algumas características quando se trata de templates, tem uma DTL – Django Language Template – um modo conveniente de gerar arquivos HTML dinamicamente, é uma alternativa do Jinja2 (django.template.backends.jinja2.Jinja2)
        'DIRS': [],  # Pode definir uma lista de diretórios onde o mecanismo deve buscar por arquivos de Template
        'APP_DIRS': True,  # APP_DIRS diz se o mecanismo deve buscar pelos arquivos de Template dentro das INSTALLED_APPS
        'OPTIONS': { # Contém configurações específicas de backend
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI é um acrônimo para interface de gateway de Servidor Web:
# Uma especificação que descreve como um servidor web se comunica com as aplicações web, e como as aplicações web podem encadear-se para processar uma requisição.
# Basicamente, trata-se de uma forma para servidores conversarem com frameworks, e vice-versa.
WSGI_APPLICATION = 'src.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Padrão
        'NAME': config('DB_NAME'),  # Nome do seu banco
        'CONN_MAX_AGE': 60,  # Para setar a persistência de conexão para 60seg
        'USER': config('DB_USER'),  # Seu usuário
        'PASSWORD': config('DB_PASSWORD'),  # Sua senha
        'HOST': config('DB_HOST'),  # inet end
        # 8000 is default #Nem precisa pôr a porta, rodará na 8000
        # (para testes)
        'PORT': '',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', #Essa validação checa a similaridade entre a senha e um conjunto de atributos do usuário. (Não pode ser a mesma que o nome do usuário etc)
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', #Checa a quantidade de caracteres, por padrão vem que não pode ser inferior a 9 (no caso 8 já que o 0 conta)
        #'OPTIONS': {
        #    'min_length': 9,
        #}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', #Verifica se a senha informada está em um arquivo que contém 1.000 senhas comuns, caso esteja você deve alterar (Ex: mypassword, password)
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', #Verifica se a senha não é completamente numérica
    },
]
# Django se preocupa com a segurança da senha dos usuários e fornece uma série de validações, acima a descrição de cada uma
# No python manage.py createsuperuser elas passam a valer


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'src', 'media')

# E-mails
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'Rafael Ribeiro <pereiraribeirorafael@gmail.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_PORT = 587

# Minhas configurações de email acima enviarão EMAIL pro user abaixo
CONTACT_EMAIL = 'pereiraribeirorafael@gmail.com'

# Auth
# Ou apenas '/conta/entrar'
LOGIN_URL = 'accounts:login'
# Quando o Django loga corretamente volta pra homepage
LOGIN_REDIRECT_URL = 'core:homepage'
