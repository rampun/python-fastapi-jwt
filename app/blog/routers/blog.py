from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session

from blog.repository import blogRepo

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


get_db = database.get_db


# show all blogs
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.get_all(db)
    # create new blog


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.create(request, db)


# get blog detail
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def view(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.show(id, response, db)


# delete blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blogRepo.destroy(id, db)


# update blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.update(id, request, db)
