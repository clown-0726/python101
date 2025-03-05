from typing import Optional, Union

from fastapi import APIRouter, Path, Query
from pydantic import BaseModel, Field, EmailStr

router_resp = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr  # 使用 EmailStr 需要 pip install pydantic[email]
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


users = {
    "user01": {"username": "user01", "password": "123123", "email": "user01@abc.com"},
    "user02": {"username": "user02", "password": "1233456", "email": "user02@abc.com"},
}


@router_resp.post("/response_model", response_model=UserOut, response_model_exclude_unset=True)
async def response_model(user: UserIn):
    """
    response_model_exclude_unset=True 表示默认值不会包含在响应中，
    仅包含实际赋值的值，如果实际给了值，则会返回
    """
    print(user.password)  # password 不会被返回
    return users["user01"]


@router_resp.post(
    "/response_model/attributes",
    response_model=Union[UserIn, UserOut]
    # response_model_include=["username", "email", "mobile"], # 必须要包含的字段
    # response_model_exclude=["mobile"], # 必须排除的字段
)
async def response_model_attributes(user: UserIn):
    del user.password  # 如果使用 Union[UserIn, UserOut]，可以删除 password
    return user
