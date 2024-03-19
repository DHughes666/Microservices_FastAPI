from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, Field, validator, Extra

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

    class Config:
        extra = 'forbid'

class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema]

    class Config:
        extra = 'forbid'

class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]