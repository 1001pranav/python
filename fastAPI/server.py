from fastapi import FastAPI, HTTPException, Depends

# TO run fastAPI 
import uvicorn

# For using middleware
from starlette.middleware.base import BaseHTTPMiddleware

#Adding CORS middleware.
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config.dependencies import get_db
from config import dependencies
from config.constants import Status
from config.requestResponse import Response, RequestToDo
from models.todo import ToDo

# List of origins that should be allowed to make requests
origins = [
    "http://localhost:3000",
    "*",  # Allow all origins
]

app = FastAPI()

# Enabling middleware for handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins or use ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.post('/todo/')
def add_todo(post: RequestToDo):
    try:
        print(post)
        todo = ToDo()
        # task=post.task, description=post.description, start_date=post.start_date, priority=post.priority)

        todo.task = post.task
        todo.description = post.description
        todo.start_date = post.start_date
        # todo.status = Status.PAUSED
        todo.priority = post.priority


        with get_db() as db:
            db.add(todo)
            db.commit()
            db.refresh(todo)
        return Response(message="Inserted Successfully", data=todo.get_dict(), status=True)
    except Exception as e:
        # sessionDB.rollback()  # Rollback on exception
        print(e)
        raise HTTPException(500, detail=str(e))
    
if __name__ == '__main__':
    uvicorn.run("server:app", host='0.0.0.0', port=8000, reload=True)
