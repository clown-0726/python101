# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from pureapp.models import News
from user.models import UserProfile


@xframe_options_exempt
@csrf_exempt
@require_http_methods(["POST"])
def post_news(request):
    post = request.POST['post'].strip()
    if post:
        user = UserProfile.objects.get(pk=1)
        News.objects.create(user=user, content=post)
        html = render_to_string('news/news_single.html', {'news': 'xxx', 'request': request})
        return HttpResponse(html)
    else:
        return HttpResponseBadRequest("内容不能为空！")


class NewsListView(ListView):
    model = News
    paginate_by = 20
    template_name = 'news/news_list.html'

    def get_queryset(self):
        return News.objects.filter(reply=False).select_related('user', 'parent').prefetch_related('liked')
