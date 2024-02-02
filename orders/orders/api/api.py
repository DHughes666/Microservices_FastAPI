from uuid import UUID
from fastapi.openapi.models import Response
from starlette import status
from http import HTTPStatus
from typing import List

from orders.app import app
from orders.api.schemas import (
    GetOrderSchema, 
    CreateOrderSchema,
    OrderItemSchema,)

order = {                   #A
    'id': 'ff0f1355-3821-4178-9567-550dec27a373',
    'status': 'completed',
    # 'created': 1740493805,
    'updated': 174049390,
    'order': [
        {
            'product': 'cappuccino',
            'size': 'medium',
            'quantity': 1
        }
    ]
}

@app.get('/orders', response_model=List[GetOrderSchema]) #B
def get_order():
    return [order]

@app.post('/orders', 
          status_code=status.HTTP_201_CREATED,
          response_model=GetOrderSchema) #C
def create_order(order_details: CreateOrderSchema):
    return order

@app.get('/orders/{order_id}', response_model=GetOrderSchema) #D
def get_order(order_id: UUID): #E
    return order

@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    return order 

@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT) #F
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    return order

@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    return order

