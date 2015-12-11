from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    '*',
]


INSTALLED_APPS += (
    # 'raven.contrib.django.raven_compat',
)


STATIC_URL = "http://static.superfast.superpun.ch/"
MEDIA_URL = "http://media.superfast.superpun.ch/"


# Sentry Settings
# https://app.getsentry.com/dobestan/superpunch/settings/install/python-django/

# RAVEN_CONFIG = {
#     'dsn': 'https://125518cfcda84a43a455db00d1190f13:4923a48de489419cb38e382e70c74ab3@app.getsentry.com/60873',
# }
