# -*- coding: utf-8 -*-
"""`django-shyurl` views."""

from django.http import HttpResponseNotFound

def blocked(request):
    return HttpResponseNotFound()
