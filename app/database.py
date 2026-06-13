from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import psycopg
from psycopg.rows import dict_row
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg.connect(
#             host="localhost",
#             dbname="fastapi",
#             user="postgres",
#             password="1234",
#             port=5432
#         )

#         print("Database connection was successful!")
#         break

#     except psycopg.Error as error:
#         print("Connecting to database failed")
#         print("Error:", error)

#         time.sleep(2)