from fastapi import APIRouter, Depends, HTTPException
from schema import todolist as schema
from dependencies import get_db
from sqlalchemy.orm import session
from models import todolist
router = APIRouter()


@router.post('/todos/', response_model=schema.ToDoList)
def createtodolist(todos : schema.ToDoListBase, db : session = Depends(get_db)):
    todos = todolist.todos(title = todos.title, description = todos.description, completed = todos.completed)
    db.add(todos)
    db.commit()
    db.refresh(todos)
    return todos

@router.get('/todos/{todos_id}', response_model=schema.ToDoList)
def gettodos(todos_id : int, db : session = Depends(get_db)):
    db_todos = db.query(todolist.todos).filter(todolist.todos.id == todos_id).first()
    if db_todos is None:
        raise HTTPException(status_code=404, detail='item not found') 
    return db_todos

@router.put('/todos/{todos_id}', response_model=schema.ToDoList)
def updatetodolist(todos_id : int, todos : schema.ToDoListBase, db : session = Depends(get_db)):
    db_todos = db.query(todolist.todos).filter(todolist.todos.id == todos_id).first()
    if db_todos is None:
        raise HTTPException(status_code=404, detail='item not found') 
    db_todos.title = todos.title
    db_todos.description = todos.description
    db_todos.completed = todos.completed
    db.commit()
    db.refresh(db_todos)
    return db_todos

@router.delete('/todos/{todos_id}', response_model=schema.ToDoList)
def deletetodolist(todos_id : int, db : session = Depends(get_db)):
    db_todos = db.query(todolist.todos).filter(todolist.todos.id == todos_id).first()
    if db_todos is None:
        raise HTTPException(status_code=404, detail='item not found')
    db.delete(db_todos)
    db.commit()
    return db_todos