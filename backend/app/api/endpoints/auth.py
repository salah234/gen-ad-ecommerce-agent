# Login and Signup

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from uuid import uuid4
from typing import Optional, List

app = FastAPI()

class AuthDetails(BaseModel):
    email: EmailStr
    password: str 

# Add auth functionality in supabaseClient.py -> signup, signin, get user token