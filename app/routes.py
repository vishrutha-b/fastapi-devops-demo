from fastapi import APIRouter, HTTPException

from app.config import settings
from app.schemas import HealthResponse, ItemRequest, ItemResponse, MessageResponse

router = APIRouter()

# In-memory store for demo purposes
_items: dict[int, ItemResponse] = {}
_counter: int = 0


@router.get("/", response_model=MessageResponse)
async def root() -> MessageResponse:
    return MessageResponse(message=f"Welcome to {settings.app_name}")


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="healthy", version=settings.version)


@router.get("/items", response_model=list[ItemResponse])
async def list_items() -> list[ItemResponse]:
    return list(_items.values())


@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int) -> ItemResponse:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return _items[item_id]


@router.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemRequest) -> ItemResponse:
    global _counter
    _counter += 1
    new_item = ItemResponse(id=_counter, **item.model_dump())
    _items[_counter] = new_item
    return new_item
