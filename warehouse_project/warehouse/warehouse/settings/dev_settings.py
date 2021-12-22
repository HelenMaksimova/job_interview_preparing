from .base import *
SECRET_KEY = 'django-insecure-o02$nzfa1a_glhg3b*5$hq_7r7lfjl1l1nhnk%!^^%#jqnvsfi'

SITE_ID = 3
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends':
#             {
#                 'handlers': ['console'],
#                 'level': 'DEBUG',
#             }
#     },
# }