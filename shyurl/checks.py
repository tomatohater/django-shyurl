# -*- coding: utf-8 -*-
"""`django-shyurl` system checks."""

from django.core.checks import Tags, register


@register(Tags.urls)
def check_shyurls(app_configs, **kwargs):
    """
    Checks `shyurl` urlpatterns for errors and warnings.
    """
    from django.urls import get_resolver
    from django.core.checks.urls import check_resolver

    resolver = get_resolver('shyurl.urlpatterns')
    warnings = check_resolver(resolver)
    for warning in warnings:
        warning.id = warning.id.replace('urls', 'shyurl')
    return warnings
