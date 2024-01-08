import base64
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from server.apps.user.models import UserProfile
from server.apps.user.cognito.actions import initiate_auth, admin_get_user
from server.apps.user.cognito import constants

import logging

logger = logging.getLogger(__name__)

User = get_user_model()


def jwt_response_payload_handler(token, user=None, request=None, issued_at=None):
    return {
        "code": 20000,
        "message": 'Success',
        "detail": '',
        "data": {
            'jwt-token': token,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'title': user.title,
            'organization': user.company,
        }
    }


def decode_token(access_token):
    token_parts = access_token.split(".")

    header = json.loads(
        base64.b64decode(token_parts[0] + "=" * ((4 - len(token_parts[0]) % 4) % 4)).decode('utf-8'))
    payload = json.loads(
        base64.b64decode(token_parts[1] + "=" * ((4 - len(token_parts[1]) % 4) % 4)).decode('utf-8'))

    return header, payload


class CustomLoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 使用 aws cognito 进行认证
        res = initiate_auth(username="admin@orbitfin.ai",
                            auth_flow=constants.USER_PASSWORD_FLOW,
                            password="Welcome!23")

        print(res["AuthenticationResult"]["AccessToken"])

        header, payload = decode_token(res["AuthenticationResult"]["AccessToken"])
        print(header)
        print(payload)
        user_info = admin_get_user(username=payload["username"])
        print(user_info)

        # 认证通过则根据更新时间戳进行同步数据
        pass

        # 查询处当前 DB 的当前用户信息
        try:
            # user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # if user.check_password(password):
            #     return user
            return UserProfile.objects.get(username=username)
        except:
            return None
