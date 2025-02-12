from db import session
from ..models.tasks import Task
from sqlalchemy.exc import NoResultFound
from uuid import UUID


def retrieve_tasks(): #Get all tasks from DB
    try:
        data = session.query(Task).all()
    except: 
        return None
    return data

def retrieve_task(id): #Get a task by id from DB
    try:
        UUID(id)
    except ValueError:
        return None
    try:
        data = session.query(Task).filter(Task.id == id).one()
    except NoResultFound:
        return None
    return data

def create_task(task): #Add a new task in the DB
    try:
        new_task = Task(title=task.title, description=task.description)
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
    except:
        return None
    return new_task

def update_task(id, task): #Update a task by id from DB
    task_to_update = retrieve_task(id)
    if task_to_update:
        if task.is_completed:
            task_to_update.is_completed = task.is_completed
        session.commit()
        session.refresh(task_to_update)
        return task_to_update
    return None

def delete_task(id): #Deleta a task from DB
    task_to_delete = retrieve_task(id)
    if task_to_delete:
        session.delete(task_to_delete)
        session.commit()
        return task_to_delete
    return None