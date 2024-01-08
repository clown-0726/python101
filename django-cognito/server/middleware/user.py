try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

WHITE_LIST_PUB = [
    '/favicon.ico',
    '/login',
    '/user/logout',
    '/user/register',
    '/user/signature_type',
    '/user/signature',
    '/user/verific_code',
    '/user/check_email_exist',
    '/user/send_email',
    '/user/user_subscriber',
    '/user/user_subscribers',
    '/user/health',
    '/filing/get_concept_hits_sum_pri',
    '/openapi/get_share_note_details'
]

WHITE_LIST_BACKEND = [
    '/admin',
    '/docs',
]


class ValidateJWTTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = []

        white_list.extend(WHITE_LIST_PUB)
        white_list.extend(WHITE_LIST_BACKEND)

        # 如果是公共 API 则移除掉 HTTP_AUTHORIZATION 防止 JWT 判断错乱
        if any([str(request.path).startswith(item) for item in white_list]):
            request.META.pop('HTTP_AUTHORIZATION', None)
            return None

        # 如果是私有 API 必须有 HTTP_AUTHORIZATION 字段
        # if request.META.get("HTTP_AUTHORIZATION", None) is None:
        #     raise NotAuthenticated()
