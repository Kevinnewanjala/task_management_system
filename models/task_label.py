from sqlalchemy import Column, Integer, ForeignKey
from database.connection import Base

class TaskLabel(Base):
    __tablename__ = "task_label"

    task_id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    label_id = Column(Integer, ForeignKey("labels.id"), primary_key=True)
