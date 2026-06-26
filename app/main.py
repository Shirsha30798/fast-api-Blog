from fastapi import FastAPI
from .database import engine, Base
from .routers import post, user, auth, vote, forgot_password, reset_password
from fastapi.middleware.cors import CORSMiddleware

# Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(forgot_password.router)
app.include_router(reset_password.router)


@app.get("/")
def root():
    return {"message": "Hello World!!!!!!"}


# render
# dpg-d8mig36rnols73cm27hg-a
# 5432
# fast_api_blog
# fast_api_blog_user
# hj042dVthScPT8k23BRBOZdvIz2Dovnu