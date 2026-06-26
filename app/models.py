from .database import Base
from sqlalchemy import String, Boolean, DateTime, func, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class Post(Base):
    __tablename__="posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    published: Mapped[bool] = mapped_column(
    Boolean,
    server_default=text("true"),
    nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
    server_default=func.now(),
    nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__="users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
    server_default=func.now(),
    nullable=False)
    
class Vote(Base):
    __tablename__="votes"
    user_id = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    post_id = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=False, primary_key=True)

class PasswordResetToken(Base):
    __tablename__="password_reset_tokens"
    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    token : Mapped[str] = mapped_column(String, nullable=False,unique=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False)
    is_used: Mapped[bool] = mapped_column(Boolean,
    server_default=text("false"),
    nullable=False)