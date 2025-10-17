"""
Django settings for blogproject project.

Proyecto final: “Sabor y Recetas – Torres Zambrano”
"""

from pathlib import Path

# --- BASE DEL PROYECTO ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD ---
SECRET_KEY = 'django-insecure-1jo!$7+^htmsi8n8=9a_&pt_palpm8d4j48746zkl!d3(&+vk0'
DEBUG = True
ALLOWED_HOSTS = []

# --- APLICACIONES INSTALADAS ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",          # App principal del blog
    "accounts",      # App de usuarios (login, registro)
    "messages_app",  # App de comentarios o mensajes
    "ckeditor",      # Editor de texto enriquecido
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- CONFIGURACIÓN PRINCIPAL ---
ROOT_URLCONF = "blogproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # carpeta de plantillas global
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blogproject.wsgi.application"

# --- BASE DE DATOS ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- VALIDACIÓN DE CONTRASEÑAS ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- IDIOMA Y ZONA HORARIA ---
LANGUAGE_CODE = "es-EC"
TIME_ZONE = "America/Guayaquil"
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS Y MULTIMEDIA ---
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "blog" / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --- RUTAS DE LOGIN / LOGOUT ---
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "pages:pages_list"
LOGOUT_REDIRECT_URL = "pages:pages_list"

# --- CLAVE PRIMARIA POR DEFECTO ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
