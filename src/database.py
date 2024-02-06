from src.config import settings

from typing import Annotated
from sqlalchemy import create_engine, String, MetaData
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)
async_engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=False)

session_factory = sessionmaker(engine)
async_session_factory = async_sessionmaker(async_engine)
