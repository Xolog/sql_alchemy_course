import asyncio

from sqlalchemy import text, insert, select, func, cast, Integer, and_

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
    def insert_data(data: list):
        with session_factory() as session:
            worker_jack = WorkerOrm(username='Jack')
            worker_michael = WorkerOrm(username='Michael')
            session.add_all([worker_jack, worker_michael])
            session.flush()
            session.add_all(data)

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
    def select_resumes_avg_compensation(like_language: str = 'Python'):
        with session_factory() as session:
            query = (
                select(
                    ResumeOrm.workload,
                    cast(func.avg(ResumeOrm.compensation), Integer).label('avg_compensation')
                )
                .select_from(ResumeOrm)
                .filter(and_(
                    ResumeOrm.title.contains(like_language),
                    ResumeOrm.compensation > 40000
                ))
                .group_by(ResumeOrm.workload)
            )
            # print(query.compile(compile_kwargs={'literal_binds': True}))
            result = session.execute(query)
            result = result.all()
            print(f'{result=}')

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

