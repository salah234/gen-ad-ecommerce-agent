# Profile, usage limits
from fastapi import FastAPI
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from typing import Optional, List

app = FastAPI()

class User(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    create_time: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc)) # 
