import asyncio

from sqlalchemy import text, insert, select

from src.models import WorkerOrm, ResumeOrm, Base
from src.database import async_engine, engine, session_factory, async_session_factory


class SyncOrm:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        engine.echo = True
        Base.metadata.create_all(engine)
        # engine.echo = True

    @staticmethod
    def insert_data():
        with session_factory() as session:
            worker_jack = WorkerOrm(username='Jack')
            worker_michael = WorkerOrm(username='Michael')
            session.add_all([worker_jack, worker_michael])
            session.flush()

            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            # worker_id = 1
            # worker_jack = session.get(WorkerOrm, worker_id)
            query = select(WorkerOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(f'{workers=}')

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
        with session_factory() as session:
            worker_michael = session.get(WorkerOrm, worker_id)
            worker_michael.username = new_username
            worker_jack = session.get(WorkerOrm, 1)
            worker_jack.username = 'Max'
            session.expire_all()

            session.commit()

    # @staticmethod
    # async def insert_data():
    #     worker_bobr = WorkerOrm(username='bobr')
    #     worker_volk = WorkerOrm(username='volk')
    #     async with async_session_factory() as session:
    #         session.add_all([worker_bobr, worker_volk])
    #         await session.commit()

