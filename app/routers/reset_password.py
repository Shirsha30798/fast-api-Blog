from fastapi import Body, FastAPI, Response, status, HTTPException,Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session
import secrets
from datetime import datetime, timedelta, timezone
from .. import database, schemas, models
from .. import utils

router = APIRouter(tags=['Authentication'])


@router.post('/reset-password')
def forgot_password(request : schemas.ReseToken, db: Session = Depends(database.get_db)):

    existing_token = db.query(models.PasswordResetToken).filter(models.PasswordResetToken.token == request.token).first()

    if existing_token is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid reset token."
    )

    if existing_token.is_used:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"This token has already been used.")
    


    if existing_token.expires_at < datetime.now(timezone.utc):

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Your token has expired")
    

    user = db.query(models.User).filter(models.User.id == existing_token.user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )


    hashed_password = utils.hash(request.new_password)
    user.password = hashed_password
    existing_token.is_used = True
    db.commit()

    return {
        "message": "Password reset successful."
    }


        