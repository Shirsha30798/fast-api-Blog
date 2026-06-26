from fastapi import Depends, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session
import secrets
from datetime import datetime, timedelta, timezone
from .. import database, schemas, models
from .. import utils


router = APIRouter(tags=['Authentication'])


def generate_token():
    token = secrets.token_urlsafe(32)
    return token



@router.post('/forgot-password')
async def forgot_password(request: schemas.ForgotPassword, db: Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.email == request.email).first()

    generated_token = ""

    if user:

        db.query(models.PasswordResetToken).filter(models.PasswordResetToken.user_id == user.id).delete(synchronize_session=False)
        db.commit()

        generated_token = generate_token()
        reset_token = models.PasswordResetToken(
        user_id=user.id,
        token=generated_token,
        expires_at= datetime.now(timezone.utc)  + timedelta(minutes=15))
        db.add(reset_token)
        db.commit()

        reset_link = f"http://localhost:8000/reset-password?token={generated_token}"

        await utils.send_email(
            recipient=user.email,
            subject="Reset your password",
            body=f"Click the link below:\n\n{reset_link}"
        )

    return {"token" : generated_token}

# Step 5: Validate

# Check:

# token exists
# token not expired
# token not already used

# Only then update password.