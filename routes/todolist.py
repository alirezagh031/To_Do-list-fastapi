from fastapi import APIRouter


router = APIRouter()


@router.post('/todos/')
def createToDoList():