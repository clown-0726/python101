"""mypython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^api-token-auth/', obtain_auth_token),  # drf 自带的 token 认证模式
    url(r'^login/', obtain_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'docs/', include_docs_urls(title="django101")),
    url(r'^user/', include('user.urls')),
    url(r'^cmd/', include('commodity.urls')),
]
