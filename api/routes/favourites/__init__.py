from fastapi import APIRouter

from . import(
    delete_favourites,
    get_favourites,
    patch_favourites,
    create_favourites
)

router = APIRouter()
router.include_router(delete_favourites.router)
router.include_router(get_favourites.router)
router.include_router(create_favourites.router)
router.include_router(patch_favourites.router)
