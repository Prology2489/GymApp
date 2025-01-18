from sqlalchemy import Boolean, Column, Integer, String


class user(Base):
    __tablename__ = 'users'

    id = Column(Integer,)