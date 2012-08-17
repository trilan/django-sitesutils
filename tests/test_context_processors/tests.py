from django.contrib.sites.models import Site, RequestSite
from django.test import TestCase, RequestFactory

from sitesutils.context_processors import site
from sitesutils.middleware import RequestSiteMiddleware


def create_request(host):
    request_factory = RequestFactory(HTTP_HOST=host)
    return request_factory.get('/')


class SiteContextProcessorTests(TestCase):

    def setUp(self):
        self.site = Site.objects.get(pk=1)
        self.middleware = RequestSiteMiddleware()

    def test_is_lazy(self):
        request = create_request('example.com')
        self.middleware.process_request(request)
        with self.assertNumQueries(0):
            context = site(request)
        with self.assertNumQueries(1):
            context['site'].domain

    def test_is_lazy(self):
        request = create_request('example.com')
        self.middleware.process_request(request)
        context = site(request)
        self.assertEqual(context['site'], self.site)

    def test_returns_request_site(self):
        request = create_request('example.com')
        context = site(request)
        self.assertIsInstance(context['site'], RequestSite)
