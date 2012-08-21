from django.conf import settings
from django.contrib.sites.models import Site


def get_site_id(request):
    if hasattr(request, 'site') and isinstance(request.site, Site):
        return request.site.pk
    try:
        return Site.objects.get(pk=settings.SITE_ID).pk
    except Site.DoesNotExist:
        return None
