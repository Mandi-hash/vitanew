# app/schemas/chat.py
from uuid import UUID
from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, ConfigDict
from app.models.chat import MessageRole
from app.schemas.chat_blocks import ChatBlock


class ChatMessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    role: MessageRole
    content: Optional[str] = None
    tool_calls: Optional[list[dict]] = None
    tool_name: Optional[str] = None
    tool_result: Optional[Any] = None
    created_at: datetime


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
    messages: list[ChatMessageOut]  # full turn, including any tool calls that happened along the way



class ChatResponse(BaseModel):
    blocks: list[ChatBlock]
    messages: list[ChatMessageOut]