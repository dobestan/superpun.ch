import os
from .application import BASE_DIR, PROJECT_ROOT


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'dist', 'static', )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'dist', 'media', )
