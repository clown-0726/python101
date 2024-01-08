from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.views import APIView
from utils.mixin import LoginRequiredMixin
from apps.commodity.serializer import CommodityEditSerializer, CommoditySerializer
from apps.commodity.models import Commodity

'''
基础的 APIView 的使用
'''


class CommodityListView(LoginRequiredMixin, APIView):
    def get(self, request, format=None):
        """得到所有的 Commodity"""
        commodities = Commodity.objects.all()[:10]
        serializer = CommoditySerializer(commodities, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """新增一个 Commodity"""
        save_data = {}
        save_data['name'] = request.data['name']
        save_data['desc'] = request.data['desc']
        save_data['owner_id'] = request.user.id

        commodity_edit_sr = CommodityEditSerializer(data=save_data)
        if commodity_edit_sr.is_valid(raise_exception=True):
            commodity_edit_sr.save()
            # commodity_edit_sr.create(commodity_edit_sr.data)
        return JsonResponse(data={'message': 'success'})


class CommodityDetailView(LoginRequiredMixin, APIView):
    def get_object(self, pk):
        try:
            return Commodity.objects.get(pk=pk)
        except Commodity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """得到一个 Commodity"""
        commodity = self.get_object(pk)
        serializer = CommoditySerializer(commodity)
        return JsonResponse(data=serializer.data)

    def put(self, request, pk, format=None):
        """更新一个 Commodity"""
        commodity = self.get_object(pk)
        save_data = {}
        save_data['name'] = request.data['name']
        save_data['desc'] = request.data['desc']
        save_data['owner_id'] = request.user.id

        # 修改的时候 serializer 需要两个参数，第一个参数是要修改的对象，第二参数是修改的内容
        serializer = CommodityEditSerializer(commodity, data=save_data)
        if serializer.is_valid():
            # save 方法调用的是 create 和 update 方法，其判断标准为是否有 instance
            serializer.save()
            # serializer.update(serializer.data)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
