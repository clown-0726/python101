from rest_framework.views import APIView
from django.http import JsonResponse

from utils.mixin import LoginRequiredMixin


class AuthTestView(LoginRequiredMixin, APIView):
    '''
    测试 LoginRequiredMixin
    '''

    def post(self, request):
        print('I am LoginRequiredMixin')
        print(request.user)
        return JsonResponse(data={'message': 'success'})
