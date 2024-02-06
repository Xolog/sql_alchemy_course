import asyncio

from sqlalchemy import text, insert

from src.database import async_engine, engine
from src.models import metadata


async def start_engine():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT 1, 2, 3 union select 4, 5, 6'))
        print(f'Database version: {res.first()}')
        # await conn.commit()


def create_tables():
    engine.echo = False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo = True


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
