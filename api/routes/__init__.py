from .users import router as users_router
from .prompts import router as prompts_router
from .favourites import router as favourites_router

__all__ = [
    "users_router",
    "prompts_router",
    "favourites_router"
]
