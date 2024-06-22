from fastapi import APIRouter

from typing import Annotated

from fastapi import Depends

from apps.services import AuthorService
from apps.schemas import SAuthorCreate

author_router = APIRouter(prefix='/authors', tags=['authors'])


@author_router.post('')
async def create_author(author: Annotated[SAuthorCreate, Depends()]):
    await AuthorService.create_author(author)
    return {'message': 'created', 'status': 201}


@author_router.get('')
async def get_all_authors():
    authors = await AuthorService.all_authors()
    return {'data': authors}
