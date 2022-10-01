from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from functools import lru_cache


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

def get_conn(psql_uri):
    engine = create_engine(psql_uri)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session()


Base = declarative_base()
# Base = declarative_base()