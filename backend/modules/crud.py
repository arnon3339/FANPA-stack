from sqlalchemy.orm import Session
from modules import models, schemas
from datetime import datetime

def get_users(db: Session, skip: int = 0, limit: int = 100):
    res = db.query(models.User).offset(skip).limit(limit).all()
    print(res)
    return res

def create_user(db: Session, user: schemas.User):
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    print(user)
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    db_user = models.User(user_name=user.name, 
                          password=user.password,
                          email=user.email,
                          nick_name=user.nick_name,
                          created_on=datetime.now().isoformat()
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user