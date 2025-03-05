from sqlalchemy.orm import DeclarativeBase


# 创建一个 Base 类，所有 ORM 模型都将继承它
class Base(DeclarativeBase):
    pass
