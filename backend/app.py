from fastapi import FastAPI
from src.routes.root import router as RootRouter
from src.routes.tasks import router as TaskRouter

import db

app = FastAPI()

app.include_router(RootRouter, tags=["root"])
app.include_router(TaskRouter, tags=["Tasks"], prefix="/v1/tasks")