from sqlalchemy import select

from apps.database import new_session, AuthorOrm, BookOrm
from apps.schemas import SBookGet, SBookCreate, SAuthorCreate, SAuthorGet


class AuthorService:
    @classmethod
    async def create_author(cls, data: SAuthorCreate) -> dict:
        async with new_session() as session:
            data_dict = data.model_dump()
            author = AuthorOrm(**data_dict)
            session.add(author)
            await session.commit()
            return {'message': 'created'}

    @classmethod
    async def all_authors(cls):
        async with new_session() as session:
            query = select(AuthorOrm)
            result = await session.execute(query)
            author_models = result.scalars().all()
            author_schemas = [SAuthorGet.model_validate(author_model) for author_model in author_models]
            return author_schemas


class BookService:

    @classmethod
    async def get_books(cls) -> dict:
        async with new_session() as session:
            query = select(BookOrm)
            result = await session.execute(query)
            book_models = result.scalars().all()
            book_schemas = [SBookGet.model_validate(book_model) for book_model in book_models]
            return {'data': book_schemas}

    @classmethod
    async def get_book_by_id(cls, book_id: int) -> dict:
        async with new_session() as session:
            query = select(BookOrm).filter(BookOrm.id == book_id)
            result = await session.execute(query)
            book_model = result.scalars().first()
            if book_model:
                book_schema = SBookGet.model_validate(book_model)
                return {'data': book_schema}
            return {'error': 'book not found!', 'status': 404}

    @classmethod
    async def create_book(cls, data: SBookCreate):
        async with new_session() as session:
            data_dict = data.model_dump()
            book = BookOrm(**data_dict)
            session.add(book)
            await session.commit()
            return {'message': 'created'}

    @classmethod
    async def get_book_by_author_id(cls, author_id: int) -> dict:
        async with new_session() as session:
            query = select(BookOrm).filter(BookOrm.author_id == author_id)
            result = await session.execute(query)
            books_models = result.scalars().all()
            books_schemas = [SBookGet.model_validate(book_model) for book_model in books_models]
            return {'data': books_schemas}
