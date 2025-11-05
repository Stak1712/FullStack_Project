from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/")
async def list_users():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.get("/{user_id}")
async def get_user(user_id: str):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
