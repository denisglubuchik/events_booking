from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix='/images',
    tags=['Images']
)


@router.post('/events')
async def add_event_image(file: UploadFile, event_id: int):
    with open(f"app/static/images/events/{event_id}.webp", "wb+") as file_obj:
        shutil.copyfileobj(file.file, file_obj)
