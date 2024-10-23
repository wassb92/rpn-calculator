import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql+asyncpg://postgres:postgres@localhost:5432/npi_db"
print("DATABASE_URL: ", DATABASE_URL)
# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/npi_db"

engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base class for declarative models
Base = declarative_base()

async def get_db():
    """
    Dependency to get the database session. Yields an async session.
    """
    async with SessionLocal() as session:
        yield session
