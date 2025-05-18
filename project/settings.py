"""
Django settings for project project.
Gerado pelo 'django-admin startproject'
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ─────────── Segurança ───────────
SECRET_KEY = "django-insecure-2p&$j@c&uk%2nlvnhn_7hji-kw9f=gnd*mn!pe&t)v1ab&j&wz"
DEBUG = True
ALLOWED_HOSTS = ["a22309068.pythonanywhere.com"]


# ─────────── Apps ───────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # apps do projecto
    "portfolio",
    "autores",
]

# (se não usar o django-extensions/graph-models, pode apagar isto)
GRAPH_MODELS = {"all_applications": True, "group_models": True}


# ─────────── Middleware ───────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "project.urls"


# ─────────── Templates ───────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],                       #  se tiver uma pasta templates global, colocar aqui
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "portfolio.context_processors.visitor_counter",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# ─────────── Base de Dados ───────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "a22309068$default",
        "USER": "a22309068",
        "PASSWORD": "Alessandra123",
        "HOST": "a22309068.mysql.pythonanywhere-services.com",
        "PORT": "3306",
    }
}


# ─────────── Validação de passwords ───────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ─────────── Internacionalização ───────────
LANGUAGE_CODE = "pt-pt"
TIME_ZONE     = "UTC"
USE_I18N      = True
USE_TZ        = True


# ─────────── Ficheiros estáticos / media ───────────
STATIC_URL  = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL   = "media/"
MEDIA_ROOT  = os.path.join(BASE_DIR, "media")


# ─────────── Redirecionamentos de autenticação ───────────
LOGIN_URL          = "login"
LOGIN_REDIRECT_URL = "portfolio:proj_list"
LOGOUT_REDIRECT_URL= "login"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
