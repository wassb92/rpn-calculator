from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.database import engine
from app.models.database import Base
from contextlib import asynccontextmanager

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Async lifespan event for the FastAPI app. 
    Creates the database tables on startup.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Lifespan context to allow FastAPI to continue running

# Initialize FastAPI app with lifespan context (@app.on_event("startup") is deprecated)
app = FastAPI(lifespan=lifespan)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router for API endpoints
app.include_router(router)
