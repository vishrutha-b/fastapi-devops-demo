from typing import Optional

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str


class MessageResponse(BaseModel):
    message: str


class ItemRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
