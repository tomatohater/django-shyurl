# -*- coding: utf-8 -*-
"""Setup file for `django-shyurl`."""

import os

import shyurl
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = "django-shyurl",
    version = shyurl.__version__,
    description = 'Some urls just don\'t want to be seen. So hide them.',
    long_description = README,
    url = 'http://github.com/tomatohater/django-shyurl',
    author = 'Drew Engelson',
    author_email = 'drew@engelson.net',
    license='MIT',
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
