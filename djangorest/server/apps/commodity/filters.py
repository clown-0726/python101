import django_filters
from django.db.models import Q
from commodity.models import Commodity


class CommodityFilter(django_filters.rest_framework.FilterSet):
    """
    Commodity 的过滤类
    """
    pricemin = django_filters.NumberFilter(name='price', help_text="最低价格", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='price', lookup_expr='lte')

    class Meta:
        model = Commodity
        fields = ['pricemin', 'pricemax']
