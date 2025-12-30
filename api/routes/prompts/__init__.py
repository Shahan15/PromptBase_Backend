from fastapi import APIRouter

from . import (
    create_prompts,
    delete_prompts,
    get_prompts,
    patch_prompts
)

router = APIRouter()
router.include_router(get_prompts.router)
router.include_router(create_prompts.router)
router.include_router(delete_prompts.router)
router.include_router(patch_prompts.router)
