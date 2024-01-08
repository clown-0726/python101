from enum import Enum


class ErrorCodeEnum(Enum):
    # 参数异常
    VALID_FAILURE = ("ex_3000", "Web params error")
    # 业务异常
    MANGO_SELECT_FAILURE = ("ex_3001", "Mango select failure")
    MANGO_INSERT_FAILURE = ("ex_3002", "Mango insert failure")
    MANGO_UPDATE_FAILURE = ("ex_3003", "Mango update failure")
    MANGO_DELETE_FAILURE = ("ex_3004", "Mango delete failure")
    RATELIMIT_FAILURE = ("ex_3005", "Rate limit failure")
