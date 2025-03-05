from typing import Optional, List
from fastapi import APIRouter, Path, Query, Form, File, UploadFile
from pydantic import BaseModel, Field

router_params = APIRouter()

"""路径参数的常见操作
"""


# 基本的路径参数
@router_params.get("/path_param/{city}")
def city(city: str, q_str: Optional[str] = None):
    return {'city': city, 'query_string': q_str}


# 文件路径类型的路径参数
@router_params.get("/path_param/{file_path:path}")
def send_file_path(file_path: str):
    return f"The file path is {file_path}"


# 路径参数的校验，通过 Path 方法
@router_params.get("/path_param/{num}")
def file_num_validate(
        num: int = Path(..., title="file num", description="file num desc", ge=0, le=10),
):
    return {"num": num}


"""查询参数的常见操作
"""


# 查询参数的基本使用
@router_params.get("/query_param")
def page_limit(page: int = 1, limit: int = None):
    return {"page": page, "limit": limit} if limit else {"page": page}


# 查询参数的布尔类型
@router_params.get("/query_param/bool")
def type_conversion(param: bool = False):
    return param


# 查询参数的校验
@router_params.get("/query_param/validations")
def query_param_validate(
        value: str = Query(..., min_length=8, max_length=16, regex="^a"),
        values: list[str] = Query(["v1", "v2"], alias="alias_name")
):
    return value, values


"""请求体和混合参数
"""


class CityInfo(BaseModel):
    province: str = Field(..., title="Beijing")
    country: str
    country_code: str = None
    population: int = Field(default=1000, title="Population", description="Population size")

    class Config:
        json_schema_extra = {
            "example": {
                "province": "Beijing",
                "country": "China",
                "country_code": "CN",
                "population": 1000,
            }
        }


# 请求体的基本使用，可以定义嵌套的 Model 来承载数据
@router_params.put('/body_param/city')
def result(city: CityInfo):
    return city.dict()


# 路径参数的混用
@router_params.put("/mix_param/{name}")
def mix_city_info(
        name: str,
        city01: CityInfo,
        city02: CityInfo,
        confirmed: int = Query(0, ge=0, description="确诊数"),
        death: int = Query(0, ge=0, description="死亡数")
):
    if name == "Shanghai":
        return {"Shanghai": {"confirmed": confirmed, "death": death}}
    return city01.dict(), city02.dict()


"""表单数据处理
"""


@router_params.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    """用 Form 类需要 pip install python-multipart"""
    return {"username": username}


"""处理文件上传
"""


@router_params.post("/file")
async def file_1(file: bytes = File(...)):
    """
    可以定义 file: List[bytes] 类型表示允许多文件上传

    使用 File 类，文件内容会以 bytes 的形式读入内存，适合于上传小文件
    """
    return {"file_size": len(file)}


@router_params.post("/upload_files")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    # 如果要上传单个文件 files: UploadFile = File(...)

    使用 UploadFile 类的优势：
    1. 文件存储在内存中，使用的内存达到阈值后，将被保存在磁盘中
    2. 适合于图片、视频等大文件
    3. 可以获取上传的文件的元数据，如文件名、创建时间等
    4. 有文件对象的异步接口
    5. 上传的文件是 Python 文件对象，可以使用 write()、read()、seek()、close() 操作

    :param files: 上传的文件列表
    :return: 返回上传的文件名列表
    """
    return {"filenames": [file.filename for file in files]}
