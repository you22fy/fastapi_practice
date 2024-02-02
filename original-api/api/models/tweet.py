from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String(140))
