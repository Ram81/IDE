"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from channels.asgi import get_channel_layer

channel_layer = get_channel_layer()
