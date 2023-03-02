from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from .. import database, schemas, models

from ..repository import userRepo

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


# create user
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepo.create(request, db,)


#  get user detail
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return userRepo.show(id, db)
