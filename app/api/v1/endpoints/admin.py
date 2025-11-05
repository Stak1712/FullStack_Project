from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.post("/directions")
async def create_direction():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
