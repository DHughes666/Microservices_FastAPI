from http import HTTPStatus
from uuid import UUID
from typing import List
import time
import uuid

from fastapi.openapi.models import Response
from fastapi import HTTPException
from starlette import status

from orders.app import app
from orders.api.schemas import (GetOrderSchema, CreateOrderSchema)

ORDERS = []

order = {
    'id': 'ff0f1355-e821-4178-9567-550dec27a373',
    'status': 'completed',
    'created': 1740493805,
    'order': [
        {
            'product': 'cappuccino',
            'size': 'medium',
            'quantity': '1',
        }
    ] 
}

@app.get('/orders', response_model=List[GetOrderSchema])
async def get_orders():
    return ORDERS

@app.post('/orders', 
          status_code=status.HTTP_201_CREATED,
          response_model=GetOrderSchema
          )
async def create_order(order_details: CreateOrderSchema):
    order = order_details.model_dump()
    order['id'] = uuid.uuid4()
    order['created'] = time.time()
    order['status'] = 'created'
    ORDERS.append(order)
    return order

@app.get('/orders/{order_id}', response_model=GetOrderSchema)
async def get_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.put('/orders/{order_id}', response_model=GetOrderSchema)
async def update_order(order_id: UUID, order_details: CreateOrderSchema):
    for order in ORDERS:
        if order['id'] == order_id:
            order.update(order_details.model_dump())
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.delete('/orders/{order_id}')
async def delete_order(order_id: UUID):
    for index, order in enumerate(ORDERS):
        if order['id'] == order_id:
            ORDERS.pop(index)
            return ('Delete successful')
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
async def cancel_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'cancelled'
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )

@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
async def pay_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'progress'
            return order
    raise HTTPException(
        status_code=404, detail=f'Order with ID {order_id} not found'
    )