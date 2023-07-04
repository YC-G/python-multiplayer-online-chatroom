from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, TEXT, DATETIME, VARCHAR, TINYINT
from sqlalchemy import Column

Base = declarative_base()

class Msg(Base):
    __tablename__ = "msg"
    id = Column(BIGINT, primary_key=True)
    content = Column(TEXT)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


class User(Base):
    __tablename__ = "user"
    id = Column(BIGINT, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    pwd = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    phone = Column(VARCHAR(11), nullable=False, unique=True)
    sex = Column(TINYINT, nullable=True)
    zodiac = Column(TINYINT, nullable=True)
    avatar = Column(VARCHAR(100), nullable=True)
    info = Column(VARCHAR(600), nullable=True)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)

