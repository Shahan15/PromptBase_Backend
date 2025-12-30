from fastapi import APIRouter

from . import (
    create_users,
    get_users,
    delete_users,
    patch_users
)

router = APIRouter()
router.include_router(get_users.router)
router.include_router(delete_users.router)
router.include_router(create_users.router)
router.include_router(patch_users.router)