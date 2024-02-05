from src.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)
async_engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=False)


