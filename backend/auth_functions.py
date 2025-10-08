from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import HTTPException

SECRET_KEY = "your-secret-key-change-this-to-something-random-and-long"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hashed_password(password : str) -> str:
    return pwd_context.hash(password)



def verify_password( password : str , hashed_pass : str) -> bool:
    return pwd_context.verify(password , hashed_pass)



def create_token(email : str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    data = {
        "sub" : email,
        "exp" : expire
    }
    
    token = jwt.encode(data , SECRET_KEY , algorithm=ALGORITHM)
    return token



def create_reset_token(id: int, email: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(id), "email": email, "exp": expire}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(f"🧩 Token payload before encoding: {payload}")
    return token


def verify_reset_token(token: str) -> str:
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id = payload.get("sub")

        if id is None:
            raise HTTPException(
            status_code=400,
            detail="Invalid Token"
        )
        
        return int(id)
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Invalid Token"
        )





def verify_token(token : str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        
        if email is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid token"
            )
        
        return email
        
    except JWTError:
        raise HTTPException(
            status_code=400,
            detail="Invalid Token"
        )
    
