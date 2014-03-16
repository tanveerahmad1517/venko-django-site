#!/usr/bin/env python

from setuptools import setup

setup(
    name='venelins_site',
    version='1.2.0',
    description='venelin.sytes.net',
    author='Venelin Stoykov',
    author_email='vkstoykov@gmail.com',
    url='http://venelin.sytes.net/',
    install_requires=[
        'Django>=1.6',
        'Pillow>=2.1.0',
        'South>=0.8.2',
        'django-extensions>=1.2.0',
        'django-ckeditor-updated==4.2.8',
        'django-imagekit>=3.0.3',
        'django_admin_bootstrapped',
        'pygments',
        #'uWSGI>=2.0.0',
        'psycopg2',
    ],
)
