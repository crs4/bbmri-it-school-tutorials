from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from biobank_manager.database import Base, engine

from biobank_manager.controllers.participants import router as participant_router

app = FastAPI(
    title="My User Service API",
    version="1.0.0",
    description="A FastAPI service with SQLAlchemy and PostgreSQL."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(participant_router, prefix="/api", tags=["Participants"])




