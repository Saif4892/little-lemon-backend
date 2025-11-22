from pathlib import Path

# ----------------------------
# BASE & SECRET
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'dev-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# ----------------------------
# INSTALLED APPS
# ----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'restaurant',  # your app
]

# ----------------------------
# MIDDLEWARE
# ----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------
# ROOT URLS & TEMPLATES
# ----------------------------
ROOT_URLCONF = 'little_lemon.urls'

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
    }
]

WSGI_APPLICATION = 'little_lemon.wsgi.application'

# ----------------------------
# DATABASE
# ----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'littlelemon_db',
        'USER': 'root',
        'PASSWORD': 'Saif@786',  # <- put your MySQL root password here
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# ----------------------------
# LANGUAGE & TIMEZONE
# ----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------
# STATIC FILES
# ----------------------------
STATIC_URL = 'static/'

# ----------------------------
# REST FRAMEWORK
# ----------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# ----------------------------
# DEFAULT AUTO FIELD (Remove Warnings)
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
