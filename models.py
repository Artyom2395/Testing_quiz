from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.sql import func
from database import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True, index=True)
    answer = Column(String)
    created_at = Column(DateTime, default=func.now())

