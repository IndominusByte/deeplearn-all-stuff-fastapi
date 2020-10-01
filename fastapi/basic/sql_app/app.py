from time import time
from fastapi import FastAPI, Request
from schemas import UserRegister, UserOut, UserUpdate, ItemCreate
from database import metadata, engine, database
from models import UserQuery, ItemQuery
from typing import List

metadata.create_all(engine)

app = FastAPI()

@app.middleware("http")
async def add_ip_address(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(round(process_time,2))
    return response

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post('/register', status_code=201)
async def register(user: UserRegister):
    user_data = user.dict(exclude={'password'})
    user_data.update({'password':user.password.get_secret_value()})
    await UserQuery.user_register(**user_data)
    return {'message':'User has been register'}

@app.get('/users', response_model=List[UserOut])
async def users():
    return await UserQuery.all_user()

@app.put('/users/{username}')
async def update_user(username: str, user_data: UserUpdate):
    user = await UserQuery.get_user(username)

    await UserQuery.update_user(user.username,user_data.username)
    return {'message':'user successfully update'}

@app.delete('/users/{username}')
async def delete_user(username: str):
    await UserQuery.get_user(username)

    await UserQuery.delete_user(username)
    return {'message':'user successfully delete'}

# ========= ITEMS ===========
@app.post('/items/{user_id}', status_code=201)
async def create_items(user_id: int, item: ItemCreate):
    user = await UserQuery.get_user_id(user_id=user_id)

    data = item.dict()
    data.update({'user_id': user.id})
    await ItemQuery.create_item(**data)
    return {'message':'item successfully created'}
