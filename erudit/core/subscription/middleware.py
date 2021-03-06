# -*- coding: utf-8 -*-

from ipware.ip import get_ip

from .models import InstitutionIPAddressRange


class SubscriptionMiddleware(object):
    """ This middleware attaches subscription information to the request object.

    This middleware attaches informations related to the subscription
    of the current user to the request object. It attaches a ``subscription_type``
    attribute to the request. This attribute can have three values: 'institution',
    'individual' or 'open_access'.
    """
    def process_request(self, request):
        # Tries to determine if the user's IP address is contained into
        # an institutional IP address range.
        ip = get_ip(request)
        ip_range = InstitutionIPAddressRange.objects \
            .select_related('institutional_account') \
            .filter(ip_start__lte=ip, ip_end__gte=ip).first()
        if ip_range is not None:
            request.subscription_type = 'institution'
            request.institutional_account = ip_range.institutional_account
            return

        # TODO: try to determine if the user has an individual account
        # request.subscription_type = 'individual'

        # In any other the user is is in open access.
        request.subscription_type = 'open_access'
