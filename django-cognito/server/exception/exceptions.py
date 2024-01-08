from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from server.exception.error_code_enum import ErrorCodeEnum
from typing import Optional

"""
APIException:
    - code
    - detail
"""


class ParameterException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Malformed request.')
    default_code = 'parse_error'


class BusinessException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Business exception.')
    default_code = 'business_exception'

    def __init__(self, error_code: Optional[ErrorCodeEnum] = None):
        if error_code is None:
            detail = self.default_detail
            self.code = self.default_code
        else:
            detail = error_code.value[1]
            self.code = error_code.value[0]

        super().__init__(detail, self.code)
