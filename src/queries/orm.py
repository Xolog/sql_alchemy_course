import asyncio

from sqlalchemy import text, insert

from src.models import WorkerOrm, ResumeOrm, Base
from src.database import async_engine, engine, session_factory, async_session_factory


def create_tables():
    Base.metadata.drop_all(engine)
    engine.echo = True
    Base.metadata.create_all(engine)
    engine.echo = True


def insert_data():
    worker_bobr = WorkerOrm(username='bobr')
    worker_volk = WorkerOrm(username='volk')
    with session_factory() as session:
        session.add_all([worker_bobr, worker_volk])
        session.commit()


async def insert_data():
    worker_bobr = WorkerOrm(username='bobr')
    worker_volk = WorkerOrm(username='volk')
    async with async_session_factory() as session:
        session.add_all([worker_bobr, worker_volk])
        await session.commit()

