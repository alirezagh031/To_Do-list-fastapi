from fastapi import APIRouter, Depends
from schema import todolist as shema
from dependencies import get_db
from sqlalchemy.orm import session
from models import todolist
router = APIRouter()


@router.post('/todos/', response_model=shema.ToDoList)
def createtodolist(todos : shema.ToDoListBase, db : session = Depends(get_db)):
    todos = todolist.todos(title = todos.title, description = todos.description, completed = todos.completed)
    db.add(todos)
    db.commit
    db.refresh(todos)
    return todos

