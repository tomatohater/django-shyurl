# -*- coding: utf-8 -*-
"""`django-shyurl` default app settings."""

from django.conf import settings
from shyurl.urls import url


SHYURL_ENABLED = getattr(settings, 'SHYURL_ENABLED', True)

SHYURL_PATTERNS = [url(pattern)
                    for pattern in getattr(settings,'SHYURL_PATTERNS', [])]
