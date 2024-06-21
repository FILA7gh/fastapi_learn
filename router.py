from fastapi import APIRouter

from typing import Annotated

from fastapi import Depends

from repository import TaskRepository
from schemas import STaskAdd, STaskId

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)

    return {'message': 'ok', 'task_id': task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {'data': tasks}

