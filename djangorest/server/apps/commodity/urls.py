from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from commodity import views

urlpatterns = [
    url(r'^auth_test$', views.AuthTestView.as_view()),
    # APIView CBV Test
    url(r'^commodity_edit$', views.CommodityDetailView.as_view()),
    url(r'^commodity_list$', views.CommodityListView.as_view()),
    path('commodity/<str:pk>/', views.CommodityDetailView.as_view()),
]

# 为了适应 path 方法的 url 传参解析
urlpatterns = format_suffix_patterns(urlpatterns)
