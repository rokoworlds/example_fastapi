from .. import model, schemas, utils
from fastapi import Body, FastAPI, status, Response, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOutResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

# we hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
# we create user
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}',  response_model=schemas.UserOutResponse)
def get_user(id: int, db: Session = Depends(get_db), ):
    user = db.query(model.User).filter(model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user with id: {id} was not found")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
