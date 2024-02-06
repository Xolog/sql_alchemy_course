import asyncio

from sqlalchemy import text, insert

from src.database import async_engine, engine, session_factory, async_session_factory
from src.models import metadata, WorkersOrm


def create_tables():
    engine.echo = False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo = True


def insert_data():
    worker_bobr = WorkersOrm(username='bobr')
    worker_volk = WorkersOrm(username='volk')
    with session_factory() as session:
        session.add_all([worker_bobr, worker_volk])
        session.commit()


async def insert_data():
    worker_bobr = WorkersOrm(username='bobr')
    worker_volk = WorkersOrm(username='volk')
    async with async_session_factory() as session:
        session.add_all([worker_bobr, worker_volk])
        await session.commit()

