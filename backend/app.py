from fastapi import FastAPI
from src.routes.root import router as RootRouter
from src.routes.tasks import router as TaskRouter
from fastapi.middleware.cors import CORSMiddleware


import db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RootRouter, tags=["root"])
app.include_router(TaskRouter, tags=["Tasks"], prefix="/v1/tasks")