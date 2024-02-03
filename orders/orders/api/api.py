import time
import uuid
from uuid import UUID
from fastapi import HTTPException
from fastapi.openapi.models import Response
from starlette import status
from http import HTTPStatus
from typing import List

from orders.app import app
from orders.api.schemas import (
    GetOrderSchema, 
    CreateOrderSchema,
    OrderItemSchema,)

ORDERS = []

order = {                   #A
    'id': 'ff0f1355-3821-4178-9567-550dec27a373',
    'status': 'completed',
    'created': 174049380,
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
    return ORDERS

@app.post('/orders', 
          status_code=status.HTTP_201_CREATED,
          response_model=GetOrderSchema) #C
def create_order(order_details: CreateOrderSchema):
    order = order_details.model_dump()
    order['id'] = uuid.uuid4()
    order['created'] = time.time()
    ORDERS.append(order)
    return order

@app.get('/orders/{order_id}', response_model=GetOrderSchema) #D
def get_order(order_id: UUID): 
    for order in ORDERS:
        if order['id'] == order_id:
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    for order in ORDERS:
        if order['id'] == order_id:
            order.update(order_details.model_dump())
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT) #F
def delete_order(order_id: UUID):
    for index, order in enumerate(ORDERS):
        if order['id'] == order_id:
            ORDERS.pop(index)
            return Response(status_code=HTTPStatus.NO_CONTENT.value)
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'cancelled'
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'progress'
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

