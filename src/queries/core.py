import asyncio

from sqlalchemy import text, insert, select, update

from src.database import async_engine, engine
from src.models import metadata_obj, workers_table


async def start_engine():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT 1, 2, 3 union select 4, 5, 6'))
        print(f'Database version: {res.first()}')
        # await conn.commit()


class SyncCore:
    @staticmethod
    def create_tables():
        engine.echo = False
        metadata_obj.drop_all(engine)
        metadata_obj.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_data():
        with engine.connect() as conn:
            # stmt = text("""INSERT INTO workers (username) VALUES
            #     ('AO Bobr'),
            #     ('OOO Volk');""")
            stmt = insert(workers_table).values(
                [
                    {'username': 'Bobr'},
                    {'username': 'Volk'},
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with engine.connect() as conn:
            query = select(workers_table)  # SELECT * FROM workers_table
            result = conn.execute(query)
            workers = result.all()
            print(f'{workers=}')

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
        with engine.connect() as conn:
            # stmt = text("UPDATE workers SET username = :new_username WHERE id = :worker_id")
            # stmt = stmt.bindparams(new_username=new_username, worker_id=worker_id)
            stmt = (
                update(table=workers_table)
                .values(username=new_username)
                # .where(workers_table.c.id == worker_id)
                .filter_by(id=worker_id)
            )
            conn.execute(stmt)

            conn.commit()
