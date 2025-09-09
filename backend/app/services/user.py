from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.scheme.user import UserCreate, UserUpdate, UserLogin
from sqlalchemy.future import select
from app.db.crud.user import UserCrud
from app.core.jwt_context import get_pwd_hash, verify_pwd

class UserService:
  @staticmethod
  async def signup(db:AsyncSession, user:UserCreate):
    if await UserCrud.get_username(db, user.username):
      raise HTTPException(status_code=400, detail="이미 있는 이름")
    
    hash_pw = await get_pwd_hash(user.password)
    user_create = UserCreate(username=user.username, password=hash_pw, email=user.email)

    try:
      db_user = await UserCrud.create_user(db, user_create)
      await db.commit()
      await db.refresh(db_user)
      return db_user
    
    except Exception:
      raise HTTPException(status_code=401, detail="잘못된 이메일 또는 비밀번호입니다")
    

  @staticmethod
  async def login(db:AsyncSession, user:UserLogin):
    db_user = await UserCrud.get_email(db, user.email)
    
    if not db_user or not await verify_pwd(user.password, db_user.password):
      raise HTTPException(status_code=401, detail="잘못된 이메일 또는 비밀번호입니다")
    