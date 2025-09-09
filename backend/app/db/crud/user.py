from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.scheme.user import UserCreate, UserUpdate
from sqlalchemy.future import select


class UserCrud:
  # Read - 조회작업
  @staticmethod
  async def get_id(user_id:int, db:AsyncSession) -> User | None:
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalar_one_or_none()
  
  # Create - 추가작업
  @staticmethod
  async def create_user(db:AsyncSession, user:UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.flush()
    return db_user

  # Delete - 삭제작업
  @staticmethod
  async def delete_user(db:AsyncSession, user_id:int):
    db_user = await db.get(User, user_id)
    if db_user:
      await db.delete(db_user)
      await db.flush()
      return db_user
    return None
  
  # Update - 수정작업
  @staticmethod
  async def update_user(user_id:int, user:UserUpdate, db:AsyncSession):
    db_user = await db.get(User, user_id)
    if db_user:
      update = user.model_dump(exclude_unset=True) #부분적으로 수정하겠다(patch작업과 연계)
      for i,j in update.items():
        setattr(db_user,i,j) # Set Attribute
      await db.flush()
      return db_user
    return None


  # username값 얻어오기
  @staticmethod
  async def get_username(db:AsyncSession, username:str):
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalar_one_or_none()

  # email 값 얻어오기
  @staticmethod
  async def get_email(db:AsyncSession, email:str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()