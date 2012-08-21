from django.conf import settings
from django.contrib.sites.models import Site
from django.test import TestCase, RequestFactory

from sitesutils.helpers import get_site_id


def create_request(site=None):
    request_factory = RequestFactory()
    request = request_factory.get('/')
    if site is not None:
        request.site = site
    return request


class GetSiteIdTests(TestCase):

    def setUp(self):
        self.site1 = Site.objects.get(id=1)
        self.site2 = Site.objects.create(
            domain='s2.example.com',
            name='s2.example.com',
        )

    def test_uses_request_site_attr(self):
        for site in (self.site1, self.site2):
            site_id = get_site_id(create_request(site))
            self.assertEqual(site_id, site.id)

    def test_uses_site_from_settings(self):
        site_id = get_site_id(create_request())
        self.assertEqual(site_id, settings.SITE_ID)
