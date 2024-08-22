from pydantic import BaseModel, Field
from config.constants import Status
from typing import Optional
 
class Response(BaseModel):
    status_code: int
    detail: str
    headers: Optional[dict] = None
    data: Optional[dict] = None

class RequestToDo(BaseModel):
    task: str
    description: str
    start_date: str 
    status: int = Field(default=Status.STARTED)
    priority: int = 1