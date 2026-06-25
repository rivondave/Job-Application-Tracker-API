from jose import JWTError, jwt

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.config import (
    SECRET_KEY,
    ALGORITHM
)

from app.models.user import User

security = HTTPBearer()


def get_current_user(
    credentials=Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = int(payload.get("sub"))

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user