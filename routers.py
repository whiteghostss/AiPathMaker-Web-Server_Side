from fastapi import APIRouter
from upload import router as upload_router
from source import router as source_router
from path import router as path_router
from package import router as package_router

router = APIRouter()
router.include_router(upload_router, prefix="/api")
router.include_router(source_router, prefix="/api")
router.include_router(path_router, prefix="/api")
router.include_router(package_router, prefix="/api") 