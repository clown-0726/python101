from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from utils.mixin import LoginRequiredMixin
from apps.commodity.serializer import CommodityEditSerializer, CommoditySerializer
from apps.commodity.models import Commodity
from apps.commodity.filters import CommodityFilter

'''
ViewSet 的使用
'''


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 1000


class CommodityListViewSet(LoginRequiredMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    pagination_class = StandardResultsSetPagination
    '''
    filter_backends 用来设置类的精确过滤，模糊搜索，数据排序
    DjangoFilterBackend 配合 filter_class 设置精确过滤，通过单独定义 Filter 类实现
    filters.SearchFilter 配合 search_fields 设置要模糊搜索的属性
    filters.OrderingFilter 配合 ordering_fields 设置数据如何排序
    '''
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CommodityFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('created_at', 'updated_at')
