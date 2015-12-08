import os
from .application import BASE_DIR, PROJECT_ROOT


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'dist', 'static', )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'dist', 'media', )


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', ),
    os.path.join(PROJECT_ROOT, 'dist', 'components', ),
)


# django-pipeline
# https://django-pipeline.readthedocs.org/en/latest/installation.html

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'


PIPELINE_JS = {
    'vendor': {
        'source_filenames': [
            'js/jquery.min.js',
            'js/bootstrap.min.js',
        ],
        'output_filename': 'js/vendor.min.js',
    },

    # 'main': {
    #     'source_filenames': {
    #         'js/application.js',
    #     },
    #     'output_filename': 'js/superpunch.min.js',
    # },
}

PIPELINE_CSS = {
    'vendor': {
        'source_filenames': [
            'css/bootstrap.min.css',
        ],
        'output_filename': 'css/vendor.min.css',
    },

    # 'main': {
    #     'source_filenames': {
    #         'css/application.css',
    #     },
    #     'output_filename': 'css/superpunch.min.css',
    # },
}
