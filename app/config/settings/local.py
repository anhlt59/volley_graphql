from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

# # config logging
# import sys
# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'stream': sys.stdout,
#         }
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'INFO',
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#         },
#     },
# }

MIDDLEWARE += ["core.middlewares.debug_query.QueryCountDebugMiddleware"]