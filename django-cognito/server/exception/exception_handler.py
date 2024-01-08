from rest_framework.views import exception_handler
from django.http import JsonResponse
import traceback

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class ExceptionGlobeMiddleware(MiddlewareMixin):
    """
    Below is the global exception handler of django
    兜底的异常捕获类
    """

    def process_exception(self, request, exception):
        # FIXME: 打印错误
        traceback.print_exc()

        # 直接抛出 django admin 的异常
        if str(request.path).startswith('/admin/'):
            return None

        # 捕获其他异常，直接返回 500
        ex_data = {
            "msg": "Sorry, we make a SEVERE ERROR (￣ ‘i ￣;) !!!",
            "error_code": 9999,
            "request": request.path
        }
        return JsonResponse(data=ex_data, status=500)


def globe_exception_handler(exc, context):
    """
    Below is the global exception handler of drf:
    Http404 / PermissionDenied / APIException
    """

    # FIXME: 打印错误堆栈
    traceback.print_exc()

    # Step 1. Call REST framework's default exception handler
    response = exception_handler(exc, context)
    request = context['request']

    # Step 2. Exceptions form DRF and Django built-in `Http404` and `PermissionDenied`
    if response is not None:
        if isinstance(response.data, list):
            msg = '; '.join(response.data)
        elif isinstance(response.data, str):
            msg = response.data
        elif isinstance(response.data, dict):
            msg = response.data["detail"]
        else:
            msg = 'Sorry, we make a mistake (*￣︶￣)!'

        ex_data = {
            "msg": msg,
            "error_code": getattr(exc, "code", "9999"),
            "request": request.path
        }
        return JsonResponse(data=ex_data, status=response.status_code)

    # Step 3. Exceptions from others
    # 如果 response 为 None 则直接触发兜底异常 ExceptionGlobeMiddleware
    return response
