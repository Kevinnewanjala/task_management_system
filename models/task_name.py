
from sqlalchemy import Column, Integer, ForeignKey
from database.connection import Base

class TaskName(Base):
    __tablename__ = "task_name"

    task_id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    name_id = Column(Integer, ForeignKey("names.id"), primary_key=True)
