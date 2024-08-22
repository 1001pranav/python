from fastapi import APIRouter, HTTPException

from config.dependencies import get_db
from config import dependencies
from config.constants import Status
from config.requestResponse import Response, RequestToDo
from models.todo import ToDo


todoRouter = APIRouter()

@todoRouter.post("/", status_code=201)
def add_todo(bodyData: RequestToDo):
    try:
        todo = ToDo(
        task=bodyData.task, description= bodyData.description, start_date=bodyData.start_date, priority=bodyData.priority)

        # todo.task = post.task
        # todo.description = post.description
        # todo.start_date = post.start_date
        # todo.status = Status.PAUSED
        # todo.priority = post.priority

        with get_db() as db:
            db.add(todo)
            db.commit()
            db.refresh(todo)
        return Response(status_code=201, detail="Inserted Successfully", data= todo.get_dict() )
    except Exception as e:
        # sessionDB.rollback()  # Rollback on exception
        print(e)
        raise HTTPException(500, detail=str(e))

@todoRouter.get('/', status_code=200)
def get_todo_list():
    try:
        with get_db() as db:
            items = db.query(ToDo).all()
            response = []
            for todoItems in items:
                response.append(todoItems.get_dict())
            return Response(status_code=200, detail="Success", data={"todo_items": response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
