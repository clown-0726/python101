from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'^auth_test$', views.AuthTestView.as_view(), name="Auth Test"),
    # url(r'^user_info$', UserInfo.as_view(), name="USERINFO"),
]
