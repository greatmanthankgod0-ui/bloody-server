import os
import shutil

from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

UPLOAD_DIR = "uploads"

@router.post("/")
async def upload_file(
    file: UploadFile = File(...)
):
    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename,
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    return {
        "success": True,
        "filename": file.filename,
        "path": filepath,
    }
