from db.base import Base
from db.session import engine
from model import user  # 确保所有模型都被导入

# 生成数据库表
Base.metadata.create_all(bind=engine)
