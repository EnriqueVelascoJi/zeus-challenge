from fastapi import APIRouter, Body, status, HTTPException
from ..schemas.tasks import TaskCreate
from ..schemas.tasks import TaskUpdate

from ..services.tasks import (
   retrieve_tasks,
   retrieve_task,
   create_task,
   update_task,
   delete_task
)

router = APIRouter()


@router.get("/")
def get_tasks():
   tasks = retrieve_tasks() 
   return tasks
      
@router.get("/{id}") 
def get_task(id): 
    task = retrieve_task(id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/")
def post_task(task: TaskCreate = Body(...)):
    new_task = create_task(task)
    if not new_task:
        raise HTTPException(status_code=400, detail="Invalid data provided.")
    return new_task


@router.put("/{id}")
def put_task(id, task: TaskUpdate = Body(...)):
    task_updated = update_task(id=id, task=task)
    if task_updated:
        return task_updated
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{id}")
def delete_task_end(id):
    task_deleted = delete_task(id=id)
    if task_deleted:
        return task_deleted
    raise HTTPException(status_code=404, detail="Task not found")