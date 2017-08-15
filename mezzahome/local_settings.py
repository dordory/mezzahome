# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "54$zkc#9e*pel0)uniz*acedov_g85(#&ns1m^0jm^*wp(f@7u"
NEVERCACHE_KEY = "ggd09j41u7k@l=$a$x-tz$uhr#y6k)94nx@0)xm9o*z#uz4(w6"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "mezzahome",
        # Not used with sqlite3.
        "USER": "aravim",
        # Not used with sqlite3.
        "PASSWORD": "mission",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "5432",
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"), "nova")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_APP_PATH, "templates", "nova")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
        },
    },
]

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = ['localhost','macbook.yun.sizebook', 'dev.aravim', ]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.
FABRIC = {
    "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": "ubuntu",  # VPS SSH username
    "HOSTS": ["localhost"],  # The IP address of your VPS
    "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": "mission",  # Live database password
    "ADMIN_PASS": "1004mong",  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
