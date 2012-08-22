import codecs
import os
from setuptools import setup, find_packages


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    return codecs.open(filepath, encoding='utf-8').read()


setup(
    name='django-sitesutils',
    version='0.1.2',
    license='ISC',
    description="Utils for Django's sites framework",
    long_description=read('README.rst'),
    url='https://github.com/trilan/django-sitesutils',
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
