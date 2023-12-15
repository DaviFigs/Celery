
from pathlib import Path
import os
import smtplib

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(xx@_172!5o7&(n07cxo%1u_rgktws+w-5k6qyde(cvrt=lk&y'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'base',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'celery_test',
        'HOST':'localhost',
        'PORT':'3306',
        'PASSWORD':'mysql',
        'USER':'root',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
else:
    STATIC_ROOT= os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CELERY_BROKER_URL = 'REDIS://127.0.0.1:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

#EMAIL CONFIG


#email: emailsenderneg
#password: emailsender123

'''class SendEmail:
    def __init__(self) -> None:
        self.email_server = smtplib.SMTP('smtp.gmail.com', 587)
        
    def __enter__(self, ):
        self.email_server.starttls()
        self.email_server.login('emailsenderneg@gmail.com', 'emailsender123')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.email_server.quit()

    def send_email(self, email, name, image):
        sender = 'emailsenderneg@gmail.com'
        recipient = [f'{email}']
        content= f'Hello {name}, You have asked for your invite some time ago\n here is!!\n{image}'
        self.email_server.sendmail(sender, recipient, content)

#   TEMOS PROBLEMAS EM TUDO, FAZER TESTES COM A CRIAÇÃO DE IMAGENS E O ENVIO DE EMALS
#   DESCOBRIR UMA FORMA SAUDÁVEL DE FAZER CRIAÇÃO DO SERVIDOR DO EMAIL SENDER
'''