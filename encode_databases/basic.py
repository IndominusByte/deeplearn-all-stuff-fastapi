import asyncio
from databases import Database
from sqlalchemy.sql import select
from sqlalchemy import MetaData, Table, Column, String, Integer, create_engine

db_url = 'sqlite:///./test.db'

database = Database(db_url, force_rollback=True)
"""
Connection options
"""
# Use an SSL connection and connection pool of between 5-20 connections
# database = Database('postgresql://localhost/example', ssl=True, min_size=5, max_size=20)
"""
Test isolation

For strict test isolation you will always want to rollback the test database to a clean state between each test case:

This will ensure that all database connections are run within a transaction that rollbacks once the database
is disconnected.
"""
# database = Database(DATABASE_URL, force_rollback=True)
"""
This will give you test cases that run against a different database to the development database,
with strict test isolation so long as you make sure to connect and disconnect to the database between test cases.
"""
# if TESTING:
#     database = Database(TEST_DATABASE_URL, force_rollback=True)
# else:
#     database = Database(DATABASE_URL)

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20), nullable=False),
    Column('fullname', String(50), nullable=False)
)

engine = create_engine(db_url, echo=True)
metadata.bind = engine
metadata.create_all(engine)

async def startup() -> None:
    # Establish the connection pool
    await database.connect()

async def shutdown() -> None:
    # Close all connection in the connection pool
    await database.disconnect()

async def create_db() -> None:
    # Execute many
    data = [
        {'name': 'oman','fullname':'pradipta'},
        {'name': 'paul','fullname':'simanjuntak'},
        {'name': 'okky','fullname':'suardhana'}
    ]

    await database.execute_many(query=users.insert(),values=data)

async def create_db_one() -> None:
    # Execute
    await database.execute(query=users.insert(),values={'name':'miky','fullname':'micky mouse'})

async def get_users() -> users:
    # Fetch multiple rows
    rows = await database.fetch_all(query=select([users]))
    return rows

async def get_user() -> users:
    # Fetch single row
    row = await database.fetch_one(query=select([users]))
    return row

async def fetch_value() -> users:
    # Fetch single value, defaults to `column=0`.
    value = await database.fetch_val(query=select([users]))
    return value

async def multiple_row() -> users:
    # Fetch multiple rows without loading them all into memory at once
    async for row in database.iterate(query=select([users])):
        print(row)

if __name__ == '__main__':
    asyncio.run(startup())
    # main function
    asyncio.run(create_db_one())
    asyncio.run(create_db())
    print(asyncio.run(get_users()))
    print()
    print(asyncio.run(get_user()))
    print()
    print(asyncio.run(fetch_value()))
    print()
    asyncio.run(multiple_row())

    asyncio.run(shutdown())
