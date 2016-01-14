# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup

name = 'django_slideshow'
version = '0.0.7'

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(
        os.path.join(os.path.abspath(__file__), os.pardir)
    )
)

install_requires = [
    "django>=1.8,<1.9",
    "django-betty-cropper==0.2.3",
    "django-jsonfield",
    "djangorestframework>=3.0",
    "djes<2.0",
    "parent-swap==0.0.4"
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
    packages=find_packages()
)
