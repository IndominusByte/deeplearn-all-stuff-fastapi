import bcrypt
from fastapi import HTTPException
from database import metadata, database
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String(100), unique=True, nullable=False),
    Column('username', String(20), nullable=False),
    Column('password', String(100), nullable=False)
)

items = Table('items', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20), nullable=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
)

class UserQuery:
    async def user_register(**data):
        hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        data.update({'password': hashed})
        user_exists = await database.fetch_one(query=select([users]).where(users.c.username == data['username']))
        if not user_exists:
            await database.execute(query=users.insert(),values=data)
        raise HTTPException(status_code=422,detail="user is exists")

    async def all_user() -> list:
        user = await database.fetch_all(query=select([users]))
        user_data = [dict(zip(x.keys(),x.values())) for x in user]
        for x in user_data:
            user_items = await database.fetch_all(query=select([items]).where(items.c.user_id == x['id']))
            x.update({'items': [dict(zip(i.keys(),i.values())) for i in [x for x in user_items]]})

        return user_data

    async def get_user(username: str):
        user = await database.fetch_one(query=select([users]).where(users.c.username == username))
        if user: return user
        raise HTTPException(status_code=404,detail="username not found")

    async def get_user_id(user_id: int):
        user = await database.fetch_one(query=select([users]).where(users.c.id == user_id))
        if user: return user
        raise HTTPException(status_code=404,detail="user id not found")

    async def update_user(old_username: str, new_username: str):
        query = users.update().values(username=new_username).where(users.c.username == old_username)
        await database.execute(query=query)

    async def delete_user(username: str):
        query = users.delete().where(users.c.username == username)
        await database.execute(query=query)


class ItemQuery:
    async def create_item(**data) -> None:
        await database.execute(query=items.insert(),values=data)
