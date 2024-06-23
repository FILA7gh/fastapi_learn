from fastapi import APIRouter

from typing import Annotated

from fastapi import Depends

from apps.services import AuthorService, BookService
from apps.schemas import SAuthorCreate, SBookCreate

author_router = APIRouter(prefix='/authors', tags=['authors'])
book_router = APIRouter(prefix='/books', tags=['books'])


@author_router.post('')
async def create_author(author: Annotated[SAuthorCreate, Depends()]):
    author = await AuthorService.create_author(author)
    return author


@author_router.get('')
async def get_all_authors():
    authors = await AuthorService.all_authors()
    return authors


@book_router.get('')
async def get_all_books():
    books = await BookService.get_books()
    return books


@book_router.get('/<int:id>')
async def get_book_by_id(book_id: int):
    book = await BookService.get_book_by_id(book_id)
    return book


@book_router.post('')
async def create_book(book: Annotated[SBookCreate, Depends()]):
    book = await BookService.create_book(book)
    return book


@book_router.get('/<int:author_id>')
async def get_books_by_author_id(author_id: int):
    books = await BookService.get_book_by_author_id(author_id)
    return books
