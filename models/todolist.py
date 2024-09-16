from database import Base
from sqlalchemy import Column, String, Integer, Boolean

class todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)