import enum
import datetime

from typing import Annotated
from sqlalchemy import ForeignKey, text, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.now(datetime.UTC))]
str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }


class WorkerOrm(Base):
    __tablename__ = 'worker'

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumeOrm(Base):
    __tablename__ = 'resume'

    id: Mapped[intpk]
    title: Mapped[str_256] = mapped_column(String(256))
    compensation: Mapped[str | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey('worker.id', ondelete='CASCADE'))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
