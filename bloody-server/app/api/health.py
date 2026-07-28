from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
async def health():
    return {
        "status": "healthy",
        "server": "Bloody Server",
        "time": datetime.utcnow().isoformat()
    }
