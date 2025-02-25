from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.v1 import ValidationError

"""
使用 Python 的类型注解来进行数据校验和 settings 管理。
Pydantic 可以在代码运行时提供类型提示，数据校验失败时提供友好的错误提示。
定义数据应该如何在纯规范的 Python 代码中保存，并用 Pydantic 验证它。
"""


# 定义 BaseModel
class User(BaseModel):
    id: int  # 必填字段
    name: str = "John"  # 选填字段，有默认值
    signup_date: Optional[datetime] = None
    friends: list[int]  # 列表中元素是 int 类型或者可以直接转换成 int 类型


if __name__ == "__main__":
    # 基本使用 -------------------------------------------------
    external_data = {
        "id": "123",
        "name": "John",
        "signup_date": "2024-02-03 12:22",
        "friends": [1, 2, "3"],
    }
    user = User(**external_data)
    print(user.id, user.name, user.signup_date, user.friends)
    print(user.dict())
    user.parse_obj(external_data)
    print(user.json())

    # 查看 schema
    print(user.schema_json())

    # 不检验数据直接创建模型类,不建议在 construct 方法去中传入未经验证的数据
    use_unverified = User.construct(**{
        "id": "hello",
        "name": "John",
        "signup_date": "2024-02-03 12:22",
        "friends": [1, 2, "3"],
    })
    print(use_unverified)

    # 字段顺序 -------------------------------------------------
    # 顺序按照定义的顺序输出
    print(user.__fields__.keys())

    # 错误友好提示 -------------------------------------------------
    try:
        User(id="123", friends=[1, 2, "Not a number"])
    except ValidationError as e:
        print(e.json())

    # 人民日报国年产业有限公司开业大吉$11111111111111从此为了谁也给过了。
    # #不检验数据直接创建模型类,不建议在construct方法去中传入未经验证的数据
