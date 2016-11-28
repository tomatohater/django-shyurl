django-shyurl
=============

A pluggable Django application that basically disables urls in a Django project.


Why?
****

This app is designed to complement ``django-unfriendly`` which obfuscates urls. ``django-shyurl`` may be used to prevent access to the original url.

Any url configured in SHYURL_PATTERNS will return a 404 error.


Installation
************

1. Install the ``django-shyurl`` package::

    pip install django-shyurl

2. Add ``shyurl`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'shyurl',
        ...
    )

3. Add some urlpatterns to block in your Django settings::

    SHYURL_PATTERNS = [
        ...
        r'^hide/$',
        r'^admin/',
        ...
    ]


Settings
********

The following may be added to your setting.py to customize the behavior of this app.

- ``SHYURL_ENABLED``

   - default: ``True``
   - Enables url blocking. When ``False``, nothing will be blocked.


 - ``SHYURL_PATTERNS``

   - default: ``[]``
   - A list of strings or regexes (Django urls format) to block.
