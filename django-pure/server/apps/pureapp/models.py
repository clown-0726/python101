from django.db import models
import uuid
from user.models import UserProfile


class News(models.Model):
    '''
    新闻表
    1）新闻可以有评论，评论用表自身存储，采用自关联
    2）新闻可以有点赞，点赞设计为与用户表的多对多关系映射
    '''
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.SET_NULL, related_name='publisher', verbose_name='USER')
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name='thread', verbose_name='SELF RELATED')
    content = models.TextField(verbose_name='CONTENT')
    liked = models.ManyToManyField(UserProfile, related_name='liked_news', verbose_name='LIKED')
    reply = models.BooleanField(default=False, verbose_name='IS REPLY')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='CREATED AT')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='UPDATED AT')

    class Meta:
        verbose_name = 'NEWS MGT'
        verbose_name_plural = verbose_name
        ordering = ("-created_at",)

    def __str__(self):
        return self.content

    def switch_liked(self, user):
        '''点赞或取消点赞'''
        if user in self.liked.all():
            self.liked.remove(user)
        else:
            self.liked.add(user)

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

    def count_liker(self):
        '''点赞数'''
        return self.liked.count()

    def get_likers(self):
        '''所有点赞用户'''
        return self.liked.all()
