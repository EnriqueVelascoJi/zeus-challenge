from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=['root']) # rot url 
def read_root():
    return {
        "status": 200,
        "mesage": "Hola estimado equipo de Zeus. Mi nombre es Enrique Velasco y esta es mi solución al Examen Técnico",
    }
