from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

    class config:
        schema_extra = {
            "example": {
                "title": "Task 1",
                "description": "Description of task 1",
            }
        }

class TaskUpdate(BaseModel):
    is_completed: bool

    class config:
        schema_extra = {
            "example": {
                "is_completed": "true"
            }
        }