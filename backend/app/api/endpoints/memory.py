# API that interacts with memory (can work for both supabase or vector DB (Maybe Chroma?))
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from typing import Optional, List, Dict

app = FastAPI()

class MemoryInfo(BaseModel):
    id: Optional[str] = Field(default_factory= lambda: str(uuid4()))
    user_id: str = Field(..., description="ID of the user doing the agent and it's memory")
    metadata: Optional[Dict[str, str]] = Field(default_factory=dict, description="Info of Current Agent's Memory")
    text: str = Field(..., description="Content of memory document from Agent")
class MemoryQueryRequest(BaseModel): # Most likely for VectorDB
    user_id: str = Field(..., description="ID of user requesting Agent's memory")
    search_text_query: str = Field(..., description="Text to search memory with")
    top_n: str = Field(..., description="Top N results to return from memory")

class MemoryQueryResponseData(BaseModel):
    id: str
    text: str
    metadata: Optional[Dict[str,str]]


class MemoryQueryResponse:
    results = List[MemoryQueryResponseData]


