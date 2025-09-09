import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, async_engine
from fastapi.concurrency import asynccontextmanager
from app.db.models import user
from app.routers import user

# 앱 시작과 종료 시 실행될 작업을 정의
@asynccontextmanager
async def lifespan(app:FastAPI):
  async with async_engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  yield
  await async_engine.dispose() # DB 연결 종료


# 앱 시작과 종료시 DB테이블 생성 및 엔진 종료 작업 실행하겠다
app = FastAPI(lifespan=lifespan)

#CORS 설정
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials = True,
  allow_methods=["*"],
  allow_headers = ["*"])

app.include_router(user.router)


# if __name__=="__main__":
#   uvicorn.run("main:app",host="127.0.0.1", poart=8081, reload=True)