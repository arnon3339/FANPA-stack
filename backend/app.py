from ctypes import Union
from functools import lru_cache
from fastapi import Depends, FastAPI
from config import Settings
from modules import dbcon, crud
from modules import schemas as model
from typing import List
from sqlalchemy.orm import Session

# dbcon.Base.metadata.create_all(bind=get)

app = FastAPI()

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()

def get_dburi(settings):
    return f"postgresql://{settings.PSQL_USER}:{settings.PSQL_PWD}@{settings.PSQL_HOST}:{settings.PSQL_PORT}/{settings.PSQL_DB}"

# Dependency
def get_db(
    settings: Settings = Depends(get_settings)
):
    dburi = get_dburi(settings)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f"xxxxx{dburi}xxxx")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    db = dbcon.get_conn(dburi)
    try:
        yield db
    finally:
        db.close()

# route is now using the Depends feature to import Settings
# @app.get("/vars")
# async def info(settings = Depends(get_settings)):
#     # db = get_db(settings)
#     # db = get_db(
#     #     user = settings.PSQL_USER,
#     #     pwd = settings.PSQL_PWD,
#     #     host = settings.PSQL_HOST,
#     #     port = settings.PSQL_PORT,
#     #     db = settings.PSQL_DB
#     # )
#     # print(db)
#     return {
#         "user" : settings.PSQL_USER,
#         "pwd" : settings.PSQL_PWD,
#         "host" : settings.PSQL_HOST,
#         "port" : settings.PSQL_PORT,
#         "db" : settings.PSQL_DB
#     }
    
    # , response_model=List[model.User]
@app.get("/", response_model=List[model.User])
async def get_all(db: Session = Depends(get_db)):
    crud.get_users(db)
    
# , response_model=model.User
@app.post("/create-user/")
async def new_user(db: Session = Depends(get_db), user: model.User = {}):
    # print(q)
    crud.create_user(db, user)
    return {}
    # pass