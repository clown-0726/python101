from typing import Optional, List
from fastapi import APIRouter, Cookie, Header

router_header = APIRouter()


# 使用 Cookie 来获取一个请求传递过来的 cookie 数据
@router_header.get("/cookie")
def cookie(cookie_id: Optional[str] = Cookie(None)):
    return {"cookie_id": cookie_id}


# 使用 Header 来获取一个请求传递过来的 header 数据
@router_header.get("/header")
def header(
        user_agent: Optional[str] = Header(None, convert_underscores=True),
        x_token: List[str] = Header([])
):
    return {"User-Agent": user_agent, "x_token": x_token}
