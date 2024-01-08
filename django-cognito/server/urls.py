from django.conf.urls import url, include
from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/login')),

    # >>>>>>>>>>>>>>>>>>>>>>>> rest_framework & JWT
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
    url(r'^verify/', verify_jwt_token),

    # >>>>>>>>>>>>>>>>>>>>>>>> custom
    url(r'^user/', include('server.apps.user.urls')),
]
