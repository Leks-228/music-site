import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# SECURITY
# -------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-key"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

# -------------------
# APPS
# -------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',

    'crispy_forms',
    'crispy_bootstrap5',

    'whitenoise.runserver_nostatic',

]

# -------------------
# MIDDLEWARE
# -------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'music_site.urls'

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

WSGI_APPLICATION = 'music_site.wsgi.application'

# -------------------
# DATABASE (FIXED)
# -------------------
db_url = os.environ.get("DATABASE_URL", "")

if isinstance(db_url, bytes):
    db_url = db_url.decode("utf-8")

if db_url:
    db_url = db_url.replace("postgres://", "postgresql://")

import os
import dj_database_url

db_url = os.environ.get("DATABASE_URL")

if not db_url:
    raise Exception("DATABASE_URL is NOT set in environment")

if isinstance(db_url, bytes):
    db_url = db_url.decode("utf-8")

db_url = db_url.strip()

if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://")

DATABASES = {
    "default": dj_database_url.parse(db_url)
}

# -------------------
# PASSWORDS
# -------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------
# LOCALIZATION
# -------------------
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# -------------------
# STATIC
# -------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------
# MEDIA (CLOUDINARY ONLY)
# -------------------
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ❗ ВАЖНО: убираем локальный media полностью
MEDIA_URL = ''
MEDIA_ROOT = ''

# -------------------
# DEFAULT AUTO FIELD
# -------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------
# CRISPY FORMS
# -------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# -------------------
# CLOUDINARY
# -------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}