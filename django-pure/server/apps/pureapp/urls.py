from django.conf.urls import url
from django.urls import path
from pureapp import views

urlpatterns = [
    url(r'', views.NewsListView.as_view()),
    url(r'post-news/', views.post_news),
    # path('post-news/', views.post_news, name='post_news'),
]
