from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from commodity import views
from commodity import views_ga
from commodity import views_vs

# 可以使用 DefaultRouter 自动映射 url
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'commodity_list_vs', views_vs.CommodityListViewSet)
# url(r'', include(router.urls)),

# 配置 viewset 的 http 方法与实际处理函数的映射关系
commodity_list = views_vs.CommodityListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    # APIView CBV Test
    url(r'^commodity_list$', views.CommodityListView.as_view()),
    path('commodity/<str:pk>/', views.CommodityDetailView.as_view()),
    # GenericAPIView
    url(r'^commodity_list_ga$', views_ga.CommodityListView.as_view()),
    # ViewSet
    url(r'^commodity_list_vs$', commodity_list),
]

# 为了适应 path 方法的 url 传参解析
urlpatterns = format_suffix_patterns(urlpatterns)
