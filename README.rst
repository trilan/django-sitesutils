Django Sites Utils
==================

.. image:: https://secure.travis-ci.org/trilan/django-sitesutils.png?branch=develop

With ``django-sitesutils`` you're able to access current site, using
``request.site`` everywhere you can access ``request`` object.

Current site is detected using host domain from ``request`` object and
``SITE_ID`` project setting as a fallback. If site is found, then
``request.site`` is set to the respective ``Site`` model object from
``django.contrib.site`` app, otherwise ``request.site`` is a
``django.contrib.sites.models.RequestSite`` instance.

Installation
------------

1. Install ``django-sitesutils`` using pip::

       $ pip install django-sitesutils

2. Add ``RequestSiteMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting::

       MIDDLEWARE_CLASSES = (
           # ...
           'sitesutils.middleware.RequestSiteMiddleware',
       )

   This middleware will set ``site`` attribute for the ``request`` object.
   This attribute is evaluated lazily, only when you access it.

3. If you want to access current site in templates, add ``site`` context
   processor to your ``TEMPLATE_CONTEXT_PROCESSORS`` settings::

       TEMPLATE_CONTEXT_PROCESSORS = (
           # ...
           'siteutils.context_processors.site',
       )

Contributing
------------

Feel free to fork, send pull requests or report bugs and issues on github.
