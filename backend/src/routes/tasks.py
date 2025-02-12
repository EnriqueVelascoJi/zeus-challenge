from fastapi import APIRouter, Body, Depends

from ..services.tasks import (

   retrieve_tasks
)

router = APIRouter()

# ------ All endpoints ----------

# @router.post("/") # SignUp user in the DB
# async def create_user(user: UserModel = Body(...)):
#     user = jsonable_encoder(user)
#     new_user = await add_user(user)
#     response = {'access_token': token, 'data': new_user }
#     return RetrieveResponse(response, "User created")

@router.get("/")
async def get_tasks():
   tasks = retrieve_tasks() ## Call the retrieve tasks service
   return tasks
      


