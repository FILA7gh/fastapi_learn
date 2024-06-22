import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

from dotenv import load_dotenv

load_dotenv()

engine = create_async_engine(os.environ.get('DATABASE_URL'))

new_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class AuthorOrm(Model):
    __table__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]


class BookOrm(Model):
    __table__ = 'books'

    id: Mapped[int]
    name: Mapped[str]
    price: Mapped[float]
    author = relationship('AuthorOrm', back_populates='books')



