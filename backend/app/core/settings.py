from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  db_user:str="root"
  db_password:str="gkxogh11@"
  db_host:str="127.0.0.1"
  db_port:str="3306"
  db_name:str="board"

  class Config:
    case_sensitive=True
    extra = "allow"
    populate_by_name = True

  @property
  def tmp_db(self) -> str:
    return f"{self.db_user}:{self.db_password.replace('@','%40')}@{self.db_host}:{self.db_port}/{self.db_name}"
    
  @property
  def db_url(self) -> str:
    return f"mysql+asyncmy://{self.tmp_db}"
  
  @property
  def sync_db_url(self) -> str:
    return f"mysql+pymysql://{self.tmp_db}"

# 전역 설정
settings = Settings()