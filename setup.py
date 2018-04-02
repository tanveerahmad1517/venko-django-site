#!/usr/bin/env python3

from setuptools import setup

setup(
    name='venelin-site',
    version='2.1.1',
    description='venelin.sytes.net',
    author='Venelin Stoykov',
    author_email='vkstoykov@gmail.com',
    url='http://venelin.sytes.net/',
    install_requires=[
        'Django>=1.11,<3',
        'Pillow>=4.3.0',
        'pilkit>=2.0',
        'django-ckeditor>=5.4.0,<6.0',
        'django-extensions>=2.0.6,<3',
        'django-appconf>=1.0.1',
        'django-imagekit>=4.0.1',
        'Pygments',
        'appenlight-client>=0.6.25',
        'psycopg2',
    ],
)
