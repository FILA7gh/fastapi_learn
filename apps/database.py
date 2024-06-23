import os
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

from dotenv import load_dotenv

load_dotenv()

# engine = create_async_engine(os.getenv('DATABASE_URL'))
engine = create_async_engine('postgresql+asyncpg://fast_user:fast_pw@database/fast_db')  # could have been hidden

new_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class AuthorOrm(Model):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

    books: Mapped[List["BookOrm"]] = relationship("BookOrm", back_populates="author")


class BookOrm(Model):

    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]

    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped["AuthorOrm"] = relationship("AuthorOrm", back_populates="books")
