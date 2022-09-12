from django.contrib.auth.mixins import AccessMixin
from rest_framework.exceptions import NotAuthenticated


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        """LoginRequired View needs HTTP_AUTHORIZATION token"""
        if request.META.get("HTTP_AUTHORIZATION", None) is None:
            raise NotAuthenticated()
        return super().dispatch(request, *args, **kwargs)
