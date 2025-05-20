from fastapi import APIRouter
from .models import gpt4, deepseek

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "MCP Server is running"}

@router.get("/models")
async def list_models():
    return {
        "available_models": [
            "gpt4",
            "deepseek"
        ]
    }