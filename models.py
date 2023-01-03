from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from database import Base

class Todo(Base):
    __tablename__ = "todo"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    done = Column(Boolean)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)