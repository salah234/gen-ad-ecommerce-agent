# API that deals with payments (Stripe checkout, billing)


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from typing import Optional, List

app = FastAPI()

class PaymentInfo(BaseModel):
    user_id: str = Field(..., description="User ID of the user making the payment") # ... means field is required
    payment_method: str = Field(..., description="Method type, (stripe, paypal, e.g.)")
    amount: float = Field(..., gt=0, description="Amount charged in USD or other currency")
    currency: float = Field(..., description="Currency type (USD, EUR, e.g.)")
    receipt_email = Optional[EmailStr] = Field(None, description="Email to send payment receipt")
    description = Optional[str] = Field(None, description="Payment Description")



# Add auth functionality in supabaseClient.py -> signup, signin, get user token