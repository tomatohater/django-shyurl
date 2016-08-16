# -*- coding: utf-8 -*-
"""`django-shyurl` middleware classes."""

from django.urls.exceptions import Resolver404

class ShyUrlMiddleware(object):
    """
    Middleware blocks any urls configured in shyurl.urlpatterns.
    """
    def __init__(self):
        from django.urls import get_resolver
        from .config import SHYURL_ENABLED
        self.resolver = get_resolver('shyurl.urlpatterns')
        self.enabled = SHYURL_ENABLED

    def process_request(self, request):
        if self.enabled:
            try:
                r = self.resolver.resolve(request.path)
                return r.func(request, *r.args, **r.kwargs)
            except Resolver404 as e:
                pass
        return None
