# -*- coding: utf-8 -*-
"""`django-shyurl` url utils."""

from django.conf.urls import url as django_url
from views import blocked


def url(regex, view=blocked):
    return django_url(regex, view)
