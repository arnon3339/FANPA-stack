from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from modules.dbcon import Base

class User(Base):
    __tablename__ = "user_data"

    user_id = Column(Integer, primary_key=True, unique=True, index=True)
    user_name = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, default=True)
    nick_name = Column(String)
    created_on = Column(TIMESTAMP)
    last_login = Column(TIMESTAMP)