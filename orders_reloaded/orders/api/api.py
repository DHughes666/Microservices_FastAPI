from datetime import datetime
from http import HTTPStatus
import uuid
from uuid import UUID

from starlette.responses import Response
from fastapi import HTTPException
from starlette import status
from typing import List, Optional

from orders.app import app
from orders.api.schemas import (
    CreateOrderSchema, GetOrderSchema, GetOrdersSchema)

ORDERS = []

order = {
    'id': 'ff0f1355-e821-4178-9567-550dec27a373',
    'status': 'delivered',
    'created': datetime.now(),
    'updated': datetime.now(),
    'order': [
        {
            'product': 'cappuccino',
            'size': 'medium',
            'quantity': 1
        }
    ]
}


@app.get('/orders', response_model=List[GetOrderSchema])
async def get_orders(
    cancelled: Optional[bool] = None, limit: Optional[int] = None):
    if cancelled is None and limit is None:
        return ORDERS
    
    query_set = [order for order in ORDERS]

    if cancelled is not None:
        if cancelled:
            query_set = [
                order for order in query_set if order['status'] == 'cancelled'
            ]
    else:
        query_set = [
            order for order in query_set if order['status'] != 'cancelled'
        ]
    if limit is not None and len(query_set) > limit:
        return query_set[:limit]
    
    return query_set

@app.post('/orders', 
          status_code=status.HTTP_201_CREATED,
          response_model=GetOrderSchema)
async def create_order(order_details: CreateOrderSchema):
    order = order_details.model_dump()
    order['id'] = uuid.uuid4()
    order['created'] = datetime.now()
    order['status'] = 'created'
    ORDERS.append(order)
    return order

@app.get('/orders/{order_id}', response_model=GetOrderSchema)
async def get_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Order with ID {order_id} not found'
    )

@app.put('/orders{order_id}', response_model=GetOrderSchema)
async def update_order(order_id: UUID, order_details: CreateOrderSchema):
    for order in ORDERS:
        if order['id'] == order_id:
            order.update(order_details.model_dump())
            return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Order with ID {order_id} not found'
    )

@app.delete('/orders/{order_id}', 
            status_code=status.HTTP_204_NO_CONTENT,
            response_class=Response)
async def delete_order(order_id: UUID):
    for index, order in enumerate(ORDERS):
        if order['id'] == order_id:
            ORDERS.pop(index)
            return Response(status_code=HTTPStatus.NO_CONTENT.value)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Order with ID {order_id} not found'
    )

@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
async def cancel_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'cancelled'
            return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Order with ID {order_id} not found'
    )

@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
async def pay_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            order['status'] = 'progress'
            return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Order with ID {order_id} not found'
    )