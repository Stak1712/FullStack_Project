from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.post("/")
async def create_interview():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.get("/{interview_id}")
async def get_interview(interview_id: str):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")

@router.post("/{interview_id}/answer")
async def submit_answer(interview_id: str):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented yet")
