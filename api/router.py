from fastapi import APIRouter

from api.routes import books
# life
api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
