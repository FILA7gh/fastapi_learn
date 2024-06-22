from pydantic import BaseModel, ConfigDict


class SAuthorCreate(BaseModel):
    name: str
    age: int


class SAuthorGet(SAuthorCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SBookCreate(BaseModel):
    name: str
    price: float
    author_id: int


class SBookGet(SBookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
