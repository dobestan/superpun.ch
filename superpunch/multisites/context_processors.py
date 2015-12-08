from django.contrib.sites.shortcuts import get_current_site


def sites(request):
    """Returns context variables related to django site framework."""
    current_site = get_current_site(request)

    return {
        'site': current_site,
        'site_profile': current_site.site_profile,
    }
