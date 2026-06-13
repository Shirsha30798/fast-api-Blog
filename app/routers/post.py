from typing import List, Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from psycopg.rows import dict_row
from .. import oauth2

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# @router.get("/")
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # with conn.cursor(row_factory=dict_row) as cursor:
        # cursor.execute("SELECT * FROM posts")
        # posts = cursor.fetchall()
    print(search)
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()


    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # print(f'this query -> {results}')
    # print(type(results))

    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    # with conn.cursor(row_factory=dict_row) as cursor:
    #     cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * ", (post.title, post.content, post.published))
    #     new_post = cursor.fetchone()
    #     conn.commit()
    new_post = models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post



# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):
    # with conn.cursor(row_factory=dict_row) as cursor:
    #         cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id),))
    #         post = cursor.fetchone()
    # post = db.get(models.Post, id)

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).filter(models.Post.id == id).group_by(models.Post.id).first()

    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} not found")

    return post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):
    
    # with conn.cursor(row_factory=dict_row) as cursor:
    #     cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id),))
    #     deleted_post = cursor.fetchone()
    #     conn.commit()

    deleted_post = db.get(models.Post, id)

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")
    
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    db.delete(deleted_post)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post : schemas.PostCreate, db: Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):
    # with conn.cursor(row_factory=dict_row) as cursor:
    #     cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    #     updated_post = cursor.fetchone()
    #     conn.commit()

    existing_post = db.get(models.Post, id)

    if existing_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")
    
    if existing_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    existing_post.title = updated_post.title
    existing_post.content = updated_post.content

    db.commit()
    db.refresh(existing_post)
                            
    return existing_post