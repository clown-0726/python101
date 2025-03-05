在设计 **FastAPI** 的大型应用程序时，良好的目录结构和分层架构能提高代码的可维护性、可扩展性和清晰度。通常，大型 FastAPI 项目会采用 **分层架构**，将代码拆分为 **API 层（接口层）、Service 层（业务逻辑层）、持久化层（数据访问层）**，并结合 **依赖注入** 和 **数据库 ORM（如 SQLAlchemy）** 进行组织。

---

## **📂 目录结构规划**
```plaintext
📦 my_fastapi_project
 ┣ 📂 app
 ┃ ┣ 📂 api                 # API 层（路由）
 ┃ ┃ ┣ 📂 v1                # API 版本管理（v1 版本）
 ┃ ┃ ┃ ┣ 📜 user.py         # 用户相关 API
 ┃ ┃ ┃ ┣ 📜 item.py         # 物品相关 API
 ┃ ┃ ┃ ┗ 📜 __init__.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 core                # 核心配置（应用配置、日志、异常处理）
 ┃ ┃ ┣ 📜 config.py         # 读取环境变量、应用配置
 ┃ ┃ ┣ 📜 security.py       # 安全相关，如 JWT 认证
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 models              # 数据模型（ORM 模型）
 ┃ ┃ ┣ 📜 user.py           # 用户表模型
 ┃ ┃ ┣ 📜 item.py           # 物品表模型
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 schemas             # Pydantic 数据校验模型
 ┃ ┃ ┣ 📜 user.py           # 用户数据模型
 ┃ ┃ ┣ 📜 item.py           # 物品数据模型
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 services            # Service 层（业务逻辑）
 ┃ ┃ ┣ 📜 user_service.py   # 用户业务逻辑
 ┃ ┃ ┣ 📜 item_service.py   # 物品业务逻辑
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 repositories        # 持久化层（数据库操作）
 ┃ ┃ ┣ 📜 user_repo.py      # 用户数据访问
 ┃ ┃ ┣ 📜 item_repo.py      # 物品数据访问
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 db                  # 数据库连接
 ┃ ┃ ┣ 📜 base.py           # SQLAlchemy 基础配置
 ┃ ┃ ┣ 📜 session.py        # 数据库 Session 依赖
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📂 deps                # 依赖注入（FastAPI Depends）
 ┃ ┃ ┣ 📜 db.py             # 数据库依赖
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 main.py             # FastAPI 入口文件
 ┃ ┗ 📜 __init__.py
 ┣ 📜 .env                  # 环境变量配置
┣ 📜 requirements.txt       # 依赖包
┣ 📜 alembic.ini            # Alembic 迁移配置
┣ 📂 migrations             # 数据库迁移文件
┗ 📜 README.md              # 项目说明
```

---

## **📌 各层职责**
### **1️⃣ API 层（app/api）**
- 负责 **路由** 和 **请求处理**，但不包含复杂的业务逻辑。
- 依赖 `service` 层来处理业务逻辑，并返回响应。

示例：`app/api/v1/user.py`
```python
from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)
```

---

### **2️⃣ Service 层（app/services）**
- 负责 **业务逻辑**，调用 `repository` 层进行数据库操作。
- 也可以进行 **数据转换、调用第三方 API** 等。

示例：`app/services/user_service.py`
```python
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user_repo import get_user_by_id, create_new_user

def create_user(db: Session, user: UserCreate):
    return create_new_user(db, user)

def get_user(db: Session, user_id: int):
    return get_user_by_id(db, user_id)
```

---

### **3️⃣ 持久化层（app/repositories）**
- 负责 **数据库操作**，如 `CRUD` 操作。
- 仅包含数据库查询，不包含业务逻辑。

示例：`app/repositories/user_repo.py`
```python
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_new_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

---

### **4️⃣ 数据模型层（app/models）**
- 负责定义数据库 `ORM` 模型（使用 `SQLAlchemy`）。

示例：`app/models/user.py`
```python
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

---

### **5️⃣ Pydantic 数据校验层（app/schemas）**
- 负责 **数据校验** 和 **序列化**，使用 `Pydantic`。

示例：`app/schemas/user.py`
```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(UserCreate):
    id: int
```

---

### **6️⃣ 数据库管理（app/db）**
- 负责 **数据库连接** 和 **Session 管理**。

示例：`app/db/session.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## **🚀 运行 FastAPI**
在 `app/main.py` 里启动 FastAPI 应用：
```python
from fastapi import FastAPI
from app.api.v1 import user

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])
```

运行：
```bash
uvicorn app.main:app --reload
```

---

## **✅ 这样设计的优势**
1. **清晰的分层架构**
   - API 负责路由，Service 负责业务逻辑，Repository 负责数据库操作，解耦代码。
2. **更易扩展**
   - 方便增加新的 API、数据库表、业务逻辑，而不会影响其他部分。
3. **更易测试**
   - Service 层和 Repository 层可以独立测试，提高代码质量。
4. **支持多数据库**
   - 通过 `repository` 层，可以轻松切换数据库（如 MySQL、PostgreSQL）。

---

## **🎯 总结**
- **API 层**：处理请求，调用 `service` 层。
- **Service 层**：处理业务逻辑，调用 `repository` 层。
- **Repository 层**：数据库 CRUD 操作。
- **Models & Schemas**：ORM 模型 & Pydantic 校验。
- **DB & Core**：数据库连接 & 配置管理。

这种架构适用于 **中大型 FastAPI 项目**，能提高可维护性、可扩展性和代码质量！🚀