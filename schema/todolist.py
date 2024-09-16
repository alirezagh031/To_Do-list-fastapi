from pydantic import BaseModel

class ToDoListBase(BaseModel):
    title : str
    description : str
    completed : bool

class ToDoList(ToDoListBase):
    id : int

    class config:
        from_attributes = True