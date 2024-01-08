import uuid
from django.db import models
from apps.user.models import UserProfile

'''
# Category - Commodity - Trolley

数据的操作和统计放在 model 中，
而将业务逻辑处理放到 view 中
'''


class Category(models.Model):
    '''
    分类表
    '''
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name='thread', verbose_name='SELF RELATED')
    content = models.TextField(verbose_name='CONTENT')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='CREATED AT')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='UPDATED AT')

    class Meta:
        verbose_name = 'NEWS MGT'
        verbose_name_plural = verbose_name
        ordering = ("-created_at",)

    def __str__(self):
        return self.content

    # def switch_liked(self, user):
    #     '''点赞或取消点赞'''
    #     if user in self.liked.all():
    #         self.liked.remove(user)
    #     else:
    #         self.liked.add(user)

    def get_parent(self):
        '''返回自关联中的上级记录或者本身'''
        if self.parent:
            return self.parent
        return self

    def get_thread(self):
        parent = self.get_parent()
        return parent.thread.all()  # 反向查询

    def comment_count(self):
        '''评论数'''
        return self.get_thread().count()  # 反向查询

    # def count_liker(self):
    #     '''点赞数'''
    #     return self.liked.count()
    #
    # def get_likers(self):
    #     '''所有点赞用户'''
    #     return self.liked.all()


class Commodity(models.Model):
    '''
    商品表
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, default=None, verbose_name="NAME")
    desc = models.TextField(null=True, verbose_name="DESC")
    price = models.IntegerField(null=True)
    owner = models.ForeignKey(UserProfile, related_name="rn_commodity_owner", null=True, on_delete=models.SET_NULL, verbose_name='COMMODITY USER ID')
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
    owner = models.ForeignKey(UserProfile, related_name="rn_trolley_owner", on_delete=models.CASCADE, verbose_name='TROLLEY USER ID')
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
