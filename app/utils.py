from pwdlib import PasswordHash
from fastapi_mail import FastMail, MessageSchema, MessageType, ConnectionConfig
from pydantic import SecretStr
import os
from . import config


password_hash = PasswordHash.recommended()

def hash(password: str):
    return password_hash.hash(password)

def verify(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

conf = ConnectionConfig(
    MAIL_USERNAME=config.settings.mail_username,
    MAIL_PASSWORD=SecretStr(os.getenv("MAIL_PASSWORD", config.settings.mail_password)),
    MAIL_FROM=config.settings.mail_from,
    MAIL_SERVER=config.settings.mail_server,
    MAIL_PORT=config.settings.mail_port,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def send_email(recipient: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[recipient],
        body=body,
        subtype=MessageType.plain
    )

    fm = FastMail(conf)

    await fm.send_message(message)
