from fastapi import FastAPI

app = FastAPI()

DUMMY_DATA = [{'name': 'john'}, {'name': 'harry'}, {'name': 'berry'}]

@app.get('/')
async def main():
    return {'message': 'Hello World'}

@app.get('/item/{name}')
async def get_name(name: str):
    return {'name': name}

@app.get('/items')
async def get_items(skip: int = 0, limit: int = 1):
    return DUMMY_DATA[skip:skip+limit]
