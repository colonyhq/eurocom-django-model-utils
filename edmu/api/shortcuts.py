from django.http import Http404

from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404


def get_object_or_permission_denied(queryset, **filter_kwargs):
    """
    Same as Django REST Framework's standard shortcut, but make sure to raise PermissionDenied if the filter_kwargs
    don't match the required types.
    """
    try:
        return get_object_or_404(queryset, **filter_kwargs)
    except Http404:
        raise PermissionDenied