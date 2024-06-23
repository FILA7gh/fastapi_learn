from contextlib import asynccontextmanager
from fastapi import FastAPI

from apps.router import author_router, book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('apps is started')
    yield
    print('power off')

app = FastAPI(lifespan=lifespan)
app.include_router(router=author_router)
app.include_router(router=book_router)
