from fastapi import APIRouter
from app.api.v1.endpoints import health, auth, users, interviews, questions, admin

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(interviews.router, prefix="/interviews", tags=["interviews"])
api_router.include_router(questions.router, prefix="/questions", tags=["questions"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
