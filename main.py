from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import delete_tables, create_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('tables deleted')
    await create_tables()
    print('tables ready')
    yield
    print('power off')

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
