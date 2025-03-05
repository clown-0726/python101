from typing import Optional
from fastapi import APIRouter, Depends

router_di = APIRouter()

"""基于函数的依赖注入
"""


async def common_parameters(q: Optional[str] = None, page: int = 1, limit: int = 10):
    return {"q": q, "page": page, "limit": limit}


# 可以用于异步的方法
@router_di.get("/dependency01")
async def dependency01(commons: dict = Depends(common_parameters)):
    return commons


# 可以用于同步的方法
@router_di.get("/dependency02")
def dependency02(commons: dict = Depends(common_parameters)):
    return commons


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, page: int = 1, limit: int = 100):
        self.q = q
        self.page = page
        self.limit = limit


@router_di.get("/classes_as_dependencies")
async def classes_as_dependencies(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    return response