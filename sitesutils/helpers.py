from django.conf import settings
from django.contrib.sites.models import Site


def get_site(request):
    if hasattr(request, 'site') and isinstance(request.site, Site):
        return request.site
    try:
        return Site.objects.get(pk=settings.SITE_ID)
    except Site.DoesNotExist:
        return None


def get_site_id(request):
    site = get_site(request)
    if site is None:
        return None
    return site.pk
