import jwt
from fastapi import HTTPException, Header
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def generate_jwt_token():
    payload = {"exp": datetime.utcnow() + timedelta(hours=2)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def authenticate(token: str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
