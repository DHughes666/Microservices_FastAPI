from enum import Enum 
from typing import List 
from uuid import UUID

from pydantic import BaseModel, Field

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
    quantity: int = Field(default=1, ge=1)

class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema]

class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: int = Field(description='Date in the form of UNIX timestamp')
    status: StatusEnum