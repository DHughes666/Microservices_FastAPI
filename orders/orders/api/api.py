from uuid import UUID
from fastapi.openapi.models import Response
from starlette import status
from http import HTTPStatus

from orders.app import app

order = {#A
    'id': 'ff0f1355-3821-4178-9567-550dec27a373',
    'status': 'completed',
    'created': 1740493805,
    'order': [
        {
            'product': 'cappuccino',
            'size': 'medium',
            'quantity': 1
        }
    ]
}

@app.get('/orders') #B
def get_order():
    return [order]

@app.post('/orders', status_code=status.HTTP_201_CREATED) #C
def create_order():
    return order

@app.get('/orders/{order_id}') #D
def get_order(order_id: UUID): #E
    return order

@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT) #F
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: UUID):
    return order

@app.post('/orders/{order_id}/pay')
def pay_order(order_id: UUID):
    return order

