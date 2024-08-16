from pydantic import BaseModel, Field
from config.constants import Status
 
class Response(BaseModel):
    message: str
    data: dict
    status: bool

class RequestToDo(BaseModel):
    task: str
    description: str
    start_date: str 
    status: int = Field(default=Status.STARTED)
    priority: int = 1