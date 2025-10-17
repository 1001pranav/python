"""
Environment-based Django settings for lms project.
"""

import os

# Determine which settings to use based on environment variable
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'local')

if ENVIRONMENT == 'production':
    from .settings.prod import *
elif ENVIRONMENT == 'uat':
    from .settings.uat import *
elif ENVIRONMENT == 'dev':
    from .settings.dev import *
else:
    from .settings.local import *