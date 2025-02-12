from db import session
from ..models.tasks import Task




# # Consultar usuarios
# usuarios = session.query(Usuario).all()
# for usuario in usuarios:
#     print(usuario.nombre, usuario.email)



def task_casting(task) -> dict: #Cast the task response
    return {
        "id": str(task["id"]),
        "title": task["title"],
        "description": task["description"],
        "is_completed": task["is_completed"]
    }




def retrieve_tasks() -> dict: # Get all tasks from DB

    tasks = []
    
    
    return tasks

