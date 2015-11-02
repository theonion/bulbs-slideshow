# -*- coding: utf-8 -*-
import os
from setuptools import setup

name = 'django_slideshow'
version = '0.0.2'

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(
        os.path.join(os.path.abspath(__file__), os.pardir)
    )
)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


install_requires = [
    "django>=1.7,<1.9",
    "django-jsonfield",
    "djangorestframework>=3.0,<4.0"
    # "parent-swap==0.0.2"
]

setup(
    name=name,
    version=version,
    description='Slideshow component for bulbs',
    license='MIT',
    author='Cameron Lowe',
    author_email='clowe@theonion.com',
    include_package_data=True,
    install_requires=install_requires,
    test_suite='django_slideshow.tests.runtests.main',
    packages=get_packages('django_slideshow'),
)
