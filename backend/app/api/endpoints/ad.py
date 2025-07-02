# Creates the Generated Ad, view history
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from typing import Optional, List

app = FastAPI()

class Ad(BaseModel):
    id: Optional[str] = None
    title: str 
    description: str
    image_url: Optional[str] = None 



# do the CRUD for ad on supabaseClient.py