from sqlalchemy.orm import Session
from model.user import User
from schema.user import UserCreate
from repo.user_repo import get_user_by_id, create_new_user

def create_user(db: Session, user: UserCreate):
    return create_new_user(db, user)

def get_user(db: Session, user_id: int):
    return get_user_by_id(db, user_id)
