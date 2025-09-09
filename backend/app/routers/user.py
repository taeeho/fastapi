from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.scheme.user import UserCreate, UserUpdate, UserLogin,UserRead
from app.services.user import UserService
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["User"])

@router.post('/signup', response_model=UserRead)
async def signup(user:UserCreate, db:AsyncSession=Depends(get_db)):
  db_user = await UserService.signup(db,user)
  return db_user

@router.post("/login", response_model=UserRead)
async def login(user:UserLogin, db:AsyncSession=Depends(get_db)):
  db_user = await UserService.login(db, user)
  return db_user
