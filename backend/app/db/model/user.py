from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
  __tablename__ = "users"
  user_id:Mapped[int] = mapped_column(primary_key=True, index=True)
  


  
