from passlib.context import CryptContext

# bcrypt는 해시 알고리즘 중 안정성이 높은편 / 패스워드 저장에 많이 쓴다
pwd_context = CryptContext(schemes=["bcrypt"])

# hash 값 저장
async def get_pwd_hash(password:str):
  return pwd_context.hash(password)

# password 검증(입력하는 비밀번호와, hash값 비밀번호가 같으면 True)
async def verify_pwd(plain_password:str, hashed_password:str):
  return pwd_context.verify(plain_password, hashed_password)