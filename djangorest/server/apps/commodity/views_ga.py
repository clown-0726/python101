from django.http import JsonResponse, Http404
from rest_framework import status, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from utils.mixin import LoginRequiredMixin
from commodity.serializer import CommodityEditSerializer, CommoditySerializer
from commodity.models import Commodity


# class CommodityListView(LoginRequiredMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Commodity.objects.all()[:10]
#     serializer_class = CommoditySerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 1000


class CommodityListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Commodity.objects.all()[:10]
    serializer_class = CommoditySerializer
    pagination_class = StandardResultsSetPagination
