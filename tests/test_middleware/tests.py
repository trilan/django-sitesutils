from django.contrib.sites.models import Site, RequestSite
from django.test import TestCase, RequestFactory

from sitesutils.middleware import RequestSiteMiddleware


def create_site(domain):
    return Site.objects.create(name=domain, domain=domain)


def create_request(host):
    request_factory = RequestFactory(HTTP_HOST=host)
    return request_factory.get('/')


class RequestSiteMiddewareTests(TestCase):

    def setUp(self):
        self.site1 = Site.objects.get(pk=1)
        self.site2 = create_site('s2.example.com')
        self.middleware = RequestSiteMiddleware()

    def test_adds_site_attr_to_request(self):
        request = create_request('example.com')
        self.middleware.process_request(request)
        self.assertTrue(hasattr(request, 'site'))

    def test_detects_site_by_domain(self):
        request = create_request('s2.example.com')
        self.middleware.process_request(request)
        self.assertEqual(request.site, self.site2)

    def test_detects_site_by_site_id_setting(self):
        request = create_request('nonexistent.example.com')
        self.middleware.process_request(request)
        self.assertEqual(request.site, self.site1)

    def test_fallbacks_to_request_site(self):
        self.site1.delete()
        request = create_request('example.com')
        self.middleware.process_request(request)
        self.assertIsInstance(request.site, RequestSite)

    def test_site_attribute_is_lazy(self):
        request = create_request('example.com')
        with self.assertNumQueries(0):
            self.middleware.process_request(request)
        with self.assertNumQueries(1):
            request.site.domain
