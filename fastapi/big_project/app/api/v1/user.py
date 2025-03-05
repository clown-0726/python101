from fastapi import APIRouter, Depends
from schema.user import UserCreate, UserResponse
from service.user_service import create_user, get_user
from db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{user_id}", response_model=UserResponse)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)
