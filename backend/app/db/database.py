from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import create_engine
from app.core.settings import settings
from sqlalchemy.orm import sessionmaker, declarative_base

async_engine = create_async_engine(settings.db_url, echo=False)

AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

engine = create_engine(settings.sync_db_url, pool_pre_ping=True)

Base = declarative_base()

async def get_db():
  session= None
  try:
    session = AsyncSessionLocal()
    yield session
  except:
    pass
  finally:
    if session:
      await session.close()
