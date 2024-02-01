from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

class SizeEnum(str, Enum): #A
    small = 'small'
    medium = 'medium'
    big = 'big'

class StatusEnum(str, Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

class OrderItemSchema(BaseModel): #B
    product: str #C
    size: SizeEnum #D
    quantity: int  = Field(default=1, ge=1) #E

class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema] 

class GetOrderSchema(CreateOrderSchema):
    id: UUID #F
    created: int = Field(description='Date in the form of UNIX timestamp') #G
    status: StatusEnum 