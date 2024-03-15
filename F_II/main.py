from fastapi import FastAPI, status

app = FastAPI()

@app.get('/')
def index():
    return 'Hello, world'

@app.get('/blog/{id}', response_description=status.HTTP_404_NOT_FOUND)
def get_blog(id: int):
    if id > 5:
        return {'error': f'Blog {id} not found'}
    return {'message': f'blog with id {id}'}