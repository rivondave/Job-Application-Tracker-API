from fastapi import FastAPI

from app.api.auth import router as auth_router

from app.core.database import Base
from app.core.database import engine

from app.models.application import (Application)

from app.api.applications import (router as applications_router)

from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Tracker API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(
    applications_router
)

@app.get("/")
def root():
    return {
        "message": "Job Tracker API Running"
    }