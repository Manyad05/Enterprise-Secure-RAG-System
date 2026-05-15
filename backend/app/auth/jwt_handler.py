from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"

def create_token(data):

    payload = data.copy()

    payload["exp"] = datetime.utcnow() + timedelta(hours=2)

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token