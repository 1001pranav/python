from sqlalchemy import Column, Integer, String, DateTime, func, Enum 
from sqlalchemy.orm import Mapped, mapped_column
from config.db import Base, engine

from config.constants import Status
class ToDo(Base):
    __tablename__="todo"

    task= Column(String(199))
    id = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    priority = Column(Integer, default=0)
    description = Column(String(1000))
    start_date = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    status= Column(Enum(Status), nullable=False, default=Status.STARTED)

    class Config:
        orm_mode = True
    
    def get_dict(self):
        return {
            "task": self.task,
            "id": self.id,
            "priority": self.priority,
            "description": self.description,
            "start_date": self.start_date,
            "created_at": self.created_at,
            "status": self.status.value
        }
    
    

# class ToDoCreate(ToDo):
#     pass  # You can add any additional fields for creation if needed

# class ToDoResponse(ToDo):
#     id: int
Base.metadata.create_all(engine)