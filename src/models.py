from sqlalchemy import MetaData, Table, Column, Integer, String

from database import Base

from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()


class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


workers_table = Table(
    'workers', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)

