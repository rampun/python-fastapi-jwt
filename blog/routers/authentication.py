from fastapi import APIRouter, Depends, HTTPException, status

from .. import schemas, database, models, JWTtoken

from datetime import timedelta


from .. hash import Hash

from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid username')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')

    access_token_expires = timedelta(
        minutes=JWTtoken.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Genereate JWT Token
