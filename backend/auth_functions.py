from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-change-this-to-something-random-and-long"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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



def verify_token(token : str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        
        if email is None:
            raise Exception("Invalid token")
        
        return email
        
    except JWTError:
        raise Exception("Invalid token")
    
