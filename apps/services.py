from sqlalchemy import select

from apps.database import new_session, AuthorOrm, BookOrm
from schemas import SBookGet, SBookCreate, SAuthorCreate, SAuthorGet


class AuthorService:
    @classmethod
    async def create_author(cls, data: SAuthorCreate) -> dict:
        async with new_session() as session:
            data_dict = data.model_dump()
            author = AuthorOrm(**data_dict)
            session.add(author)
            await session.commit()
            return {'message': 'created', 'status': 201}

    @classmethod
    async def all_authors(cls):
        async with new_session() as session:
            query = select(AuthorOrm)
            result = await session.execute(query)
            author_models = result.scalars().all()
            author_schemas = [SAuthorGet.model_validate(author_model) for author_model in author_models]
            return author_schemas
