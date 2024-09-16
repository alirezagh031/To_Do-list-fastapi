from fastapi import FastAPI
from routes import todolist

app = FastAPI()
app.include_router(todolist.router, tags=['todos'])