from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, Field, validator

class SizeEnum(str, Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'

class StatusEnum(str, Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

class OrderItemSchema(BaseModel):
    product: str
    size: SizeEnum
    quantity: int = Field(ge=1, le=1000000, default=1)

    @validator('quantity')
    def quantity_non_nullable(cls, value):
        assert value is not None, 'quantity may not be None'
        return value

class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema]

class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]