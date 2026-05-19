from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str


class MessageResponse(BaseModel):
    message: str


class ItemRequest(BaseModel):
    name: str
    description: str | None = None
    price: float


class ItemResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
