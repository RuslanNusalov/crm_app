from fastapi import APIRouter, Depends
from schemas import SNote, SNoteAdd, SNoteId
from typing import Annotated
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)    



@router.post("")
async def add_task(
        task: Annotated[SNoteAdd, Depends()],

) -> SNoteId:   
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[SNote]:
    tasks = await TaskRepository.find_all()
    return tasks
