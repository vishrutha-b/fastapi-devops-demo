import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.routes import router

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
