import uuid
from django.db import models
from user.models import UserProfile

'''
# Trolley - Commodity
数据的操作和统计放在 model 中，
而将业务逻辑处理放到 view 中
'''


class Commodity(models.Model):
    '''
    商品表
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, default=None, verbose_name="NAME")
    desc = models.TextField(null=True, verbose_name="DESC")
    price = models.IntegerField(null=True)
    owner = models.ForeignKey(UserProfile, related_name="commodity_user_id", null=True, on_delete=models.SET_NULL, verbose_name='COMMODITY USER ID')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='CREATE TIME')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='UPDATE TIME')

    class Meta:
        verbose_name = "Commodity"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Trolley(models.Model):
    '''
    购物车表
    购物车可以有 -> 子购物车
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, default=None, verbose_name="NICK NAME")
    desc = models.CharField(max_length=254, unique=True, null=False, verbose_name="EMAIL")
    owner = models.ForeignKey(UserProfile, related_name="trolley_user_id", on_delete=models.CASCADE, verbose_name='TROLLEY USER ID')
    # 与 Commodity 多对多关系映射
    commodity = models.ManyToManyField(Commodity, related_name='to_commodity', verbose_name='TO COMMODITY')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='CREATE TIME')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='UPDATE TIME')

    class Meta:
        verbose_name = "Trolley"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def switch_commodity(self, commodity):
        '''
        如果商品不在购物车，则加入，如果在，则移除
        '''
        if commodity in self.commodity.all():
            self.commodity.remove(commodity)
        else:
            self.commodity.add(commodity)

    def get_parent(self):
        '''
        得到自关联的父记录
        如果有值，则自己就是父记录，直接返回
        '''
        if self.parent:
            return self.parent
        else:
            return self
