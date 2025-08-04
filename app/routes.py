from fastapi import APIRouter

router = APIRouter()

@router.get("/api/message")
def get_message():
    return {"message": "Hello from Python Web Application!"}
